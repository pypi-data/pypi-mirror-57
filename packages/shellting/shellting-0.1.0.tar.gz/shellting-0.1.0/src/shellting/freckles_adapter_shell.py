# -*- coding: utf-8 -*-
import logging

from freckles.adapters import FrecklesAdapter
from freckles.defaults import (
    VARS_KEY,
    FRECKLET_KEY_NAME,
    FRECKLES_DESC_METADATA_KEY,
    FRECKLES_DESC_SHORT_METADATA_KEY,
)
from frutils.config import Cnf
from shellting.defaults import DEFAULT_SHELLTINGS_FOLDER
from shellting.processors import ShelltingProcessor
from shellting.shell_runner import ShellRunner
from shellting.shellting import ShelltingContext

log = logging.getLogger("freckles")

SHELL_CONFIG_SCHEMA = {}
SHELL_RUN_CONFIG_SCHEMA = {
    "ssh_key": {
        "type": "string",
        "doc": {"short_help": "the path to a ssh key identity file"},
        # "target_key": "ansible_ssh_private_key_file",
    },
    "user": {
        "type": "string",
        "doc": {"short_help": "the user name to use for the connection"},
    },
    "connection_type": {
        "type": "string",
        "doc": {"short_help": "the connection type, probably 'ssh' or 'local'"},
        # "target_key": "ansible_connection",
    },
    "port": {
        "type": "integer",
        "default": 22,
        "doc": {"short_help": "the ssh port to connect to in case of a ssh connection"},
        "target_key": "ssh_port",
    },
    "host": {
        "type": "string",
        "doc": {"short_help": "the host to connect to"},
        "default": "localhost",
        # "target_key": "host"
    },
    "host_ip": {"type": "string", "doc": {"short_help": "the host ip, optional"}},
    "elevated": {
        "type": "boolean",
        "doc": {"short_help": "this run needs elevated permissions"},
        "target_key": "elevated_permissions_required",
    },
    "passwordless_sudo": {
        "type": "boolean",
        "target_key": "passwordless_sudo_possible",
        "doc": {
            "short_help": "the user can do passwordless sudo on the host where those tasks are run"
        },
    },
    "no_run": {
        "type": "boolean",
        "coerce": bool,
        "doc": {
            "short_help": "only create the Ansible environment, don't execute any playbooks"
        },
    },
}


class FrecklesAdapterShell(FrecklesAdapter):
    def __init__(self, name, context):

        super(FrecklesAdapterShell, self).__init__(
            adapter_name=name,
            context=context,
            config_schema=SHELL_CONFIG_SCHEMA,
            run_config_schema=SHELL_RUN_CONFIG_SCHEMA,
        )

        self._shellting_context = None
        self._processors = {}

    def get_processor(self, proc_name):

        if proc_name in self._processors.keys():

            return self._processors[proc_name]

        if proc_name == "shellting":
            proc = ShelltingProcessor(self._shellting_context.shellting_index)
        else:
            raise Exception("No processor for type: {}".format(proc_name))

        self._processors[proc_name] = proc

        return self._processors[proc_name]

    @property
    def shellting_context(self):

        if self._shellting_context is None:
            repo_list = self.resource_folder_map.get("shellting")

            if not repo_list:
                repo_list = []

            repos = []
            for r in repo_list:
                repos.append(r["path"])

            cnf = Cnf(self.context.config)

            self._shellting_context = ShelltingContext("default", cnf, repos=repos)

        return self._shellting_context

    def get_resources_for_task(self, task):

        pass

    def get_folders_for_alias(self, alias):

        if alias == "default":
            return [DEFAULT_SHELLTINGS_FOLDER]
        return []

    def get_supported_resource_types(self):

        return ["shellting"]

    def get_supported_task_types(self):

        return ["shellting"]

    def get_extra_frecklets(self):

        result = {}
        for (
            shellting_name,
            shellting,
        ) in self.shellting_context.shellting_index.items():

            if shellting.meta.get("meta", {}).get("freckles", {}).get("ignore", False):
                continue

            try:
                frecklet = {}
                frecklet["args"] = shellting.args
                frecklet["doc"] = shellting.doc.exploded_dict()

                f_vars = {}
                for k in shellting.args.keys():
                    f_vars[k] = "{{{{:: {} ::}}}}".format(k)

                f_dict = {"type": "shellting", "name": shellting_name}
                f = {FRECKLET_KEY_NAME: f_dict, VARS_KEY: f_vars}

                frecklet["frecklets"] = [f]

                result[shellting_name] = frecklet
            except (Exception) as e:
                log.warning(
                    "Could not process shellting '{}': {}".format(shellting_name, e)
                )

        return result

    def prepare_execution_requirements(self, run_config, task_list, parent_task):

        pass

    def run(
        self,
        tasklist,
        run_vars,
        run_config,
        run_secrets,
        run_env,
        result_callback,
        parent_task,
    ):

        runner = ShellRunner(shellting_context=self.shellting_context)

        commands = []
        functions = {}
        for task in tasklist:

            task_type = task[FRECKLET_KEY_NAME]["type"]

            proc = self.get_processor(task_type)
            processed = proc.process_task(task)

            processed["_id"] = task[FRECKLET_KEY_NAME]["_task_id"]
            processed["_name"] = task[FRECKLET_KEY_NAME]["name"]
            processed["_msg"] = (
                task[FRECKLET_KEY_NAME]
                .get(FRECKLES_DESC_METADATA_KEY, {})
                .get(FRECKLES_DESC_SHORT_METADATA_KEY, processed["_name"])
            )

            functions = processed.pop("functions")
            for f_n, f in functions.items():
                if f_n not in functions.keys():
                    functions[f_n] = f

            commands.append(processed)

        run_properties = runner.render_environment(
            run_env_dir=run_env["env_dir"], commands=commands, functions=functions
        )

        run_properties = runner.run(
            run_cnf=run_config,
            run_properties=run_properties,
            result_callback=result_callback,
            parent_task=parent_task,
        )

        return run_properties
