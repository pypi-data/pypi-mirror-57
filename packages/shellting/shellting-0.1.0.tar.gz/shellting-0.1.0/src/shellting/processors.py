# -*- coding: utf-8 -*-
import abc
import logging

import six

from freckles.defaults import TASK_KEY_NAME, VARS_KEY, FRECKLET_KEY_NAME

log = logging.getLogger("freckles")


@six.add_metaclass(abc.ABCMeta)
class ShellTaskTypeProcessor(object):
    def __init__(self):
        pass

    @abc.abstractmethod
    def process_task(self, task):
        """Takes a task description, returns a list of shell script parts incl. optional external dependencies."""

        pass


# class ShellCommandProcessor(ShellTaskTypeProcessor):
#     def __init__(self):
#
#         super(ShellCommandProcessor, self).__init__()
#
#     def process_task(self, task):
#
#         # if "command" in task["task"].keys():
#         #     command = task["task"]["command"]
#         # else:
#         #     command = task["task"].get("name")
#         command = task[TASK_KEY_NAME]["command"]
#
#         task_id = task[TASK_KEY_NAME]["_task_id"]
#
#         command_tokens = task[TASK_KEY_NAME].get("command_tokens", [])
#
#         vars = task.get(VARS_KEY, {})
#         args = []
#         for token in command_tokens:
#             if token not in vars.keys():
#                 raise Exception("Token '{}' not available in vars")
#             if vars[token]:
#                 args.append(vars[token])
#
#         desc = task[FRECKLET_KEY_NAME].get(
#             FRECKLES_DESC_METADATA_KEY, {FRECKLES_DESC_SHORT_METADATA_KEY: command}
#         )
#         return {
#             "tasks": [
#                 {
#                     "command": command,
#                     "args": args,
#                     "type": task[FRECKLET_KEY_NAME]["type"],
#                     FRECKLES_DESC_METADATA_KEY: desc,
#                     "id": task_id,
#                 }
#             ],
#             "files": {},
#             "functions": {},
#         }


class ShelltingProcessor(ShellTaskTypeProcessor):
    def __init__(self, shellting_index):
        super(ShelltingProcessor, self).__init__()
        self.shellting_index = shellting_index

    def get_all_dependency_shelltings(
        self, shellting, incl_shellting=True, result=None
    ):

        if result is None:
            result = {}

        if shellting in result.keys():
            return result

        if incl_shellting:
            result[shellting.id] = shellting

        for res_type, res_names in shellting.resources.items():

            for res_name in res_names:
                if res_name not in result.keys():
                    result[res_name] = self.shellting_index.get(res_name)
                    self.get_all_dependency_shelltings(res_name, result=result)

        return result

    def process_task(self, task):

        shellting_name = task[TASK_KEY_NAME]["command"]
        shellting = self.shellting_index.get(shellting_name)

        functions = self.get_all_dependency_shelltings(shellting)

        command = shellting_name

        return {
            "functions": functions,
            "command": command,
            "args": task[VARS_KEY],
            "task_id": task[FRECKLET_KEY_NAME]["_task_id"],
            "task_desc": task[FRECKLET_KEY_NAME]
            .get("desc", {})
            .get("short", task[FRECKLET_KEY_NAME]["name"]),
            "task_name": task[FRECKLET_KEY_NAME]["name"],
        }


# class ShellScriptTemplateProcessor(ShellTaskTypeProcessor):
#     def __init__(self):
#         super(ShellScriptTemplateProcessor, self).__init__()
#
#         # self.scrptling_index = scriptling_index
#
#     def process_task(self, task):
#
#         template_script = task[TASK_KEY_NAME]["command"]
#
#         content = task[TASK_KEY_NAME]["script"]
#
#         task_id = task[FRECKLET_KEY_NAME]["_task_id"]
#
#         command_name = "{}_{}".format(template_script, task_id)
#
#         ext_file = {}
#         ext_file["type"] = "string_content"
#         ext_file["content"] = content
#
#         command_desc = {"commands": [], "files": {}, "functions": {}}
#         command_desc["commands"].append([command_name])
#         command_desc["files"][command_name] = ext_file
#
#         return command_desc
