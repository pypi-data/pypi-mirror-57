# -*- coding: utf-8 -*-

"""Main module."""

import logging
import os
import sys

from jinja2 import FileSystemLoader, Environment

from frutils.jinja2_filters import ALL_FILTERS
from shellting.defaults import DEFAULT_SHELLTINGS_FOLDER, SHELLTING_LOAD_CONFIG
from ting.tings import TingTings

log = logging.getLogger("shellting")


def generate_jinja_env(template_dir):

    template_filters = ALL_FILTERS

    jinja_env = Environment(loader=FileSystemLoader(template_dir))

    if template_filters:
        for tn, tf in template_filters.items():
            jinja_env.filters[tn] = tf["func"]

    return jinja_env


class ShelltingContext(object):
    def __init__(self, context_name, cnf, repos):

        self._context_name = context_name
        self._cnf = cnf
        self.repos = repos
        self.repos = [DEFAULT_SHELLTINGS_FOLDER]
        self._shellting_index = None
        self._jinja_env = None

        if not hasattr(sys, "frozen"):
            self.default_template_dir = os.path.join(
                os.path.dirname(__file__), "templates"
            )
        else:
            self.default_template_dir = os.path.join(
                sys._MEIPASS, "shellting", "templates"
            )
        log.debug("shellting template folder: {}".format(self.default_template_dir))

    @property
    def shellting_index(self):

        if self._shellting_index is not None:
            return self._shellting_index

        folder_index_conf = []
        used_aliases = []

        for f in self.repos:

            url = f

            alias = os.path.basename(url).split(".")[0]
            i = 1
            while alias in used_aliases:
                i = i + 1
                alias = "{}_{}".format(alias, i)

            used_aliases.append(alias)
            folder_index_conf.append(
                {"repo_name": alias, "folder_url": url, "loader": "script_files"}
            )

        self._shellting_index = TingTings.from_config(
            "shelltings",
            folder_index_conf,
            SHELLTING_LOAD_CONFIG,
            indexes=["shellting_name"],
        )
        return self._shellting_index

    def jinja_env(self, template_dir=None):

        if template_dir is None:
            if self._jinja_env is not None:
                return self._jinja_env

            self._jinja_env = generate_jinja_env(template_dir=self.default_template_dir)
            return self._jinja_env

        else:
            return generate_jinja_env(template_dir=template_dir)

    def get_template(self, template_name, template_dir=None):

        jinja_env = self.jinja_env(template_dir=template_dir)

        template = jinja_env.get_template(name=template_name)
        return template

    def render_script(self, shellting_name, args=None):

        shellting = self.get_shellting(shellting_name)

        functions = []
        for res_type, res_names in shellting.resources.items():

            if res_type == "shellting":
                for res_name in res_names:
                    func = self.get_shellting(res_name)
                    functions.append(func)

        functions.append(shellting)

        if args is None:
            args = {}

        template = self.get_template("script.j2")
        extra_repl_dict = {"skip_shebang": False, "functions": functions, "args": args}

        src = shellting.render_template(
            ting_repl_name="shellting",
            template=template,
            extra_repl_dict=extra_repl_dict,
        )

        # command = [shellting.id]
        # for k, v in user_input.items():
        #     command.append("--{}".format(k))
        #     command.append('"{}"'.format(v))

        return src

    def get_shellting(self, shellting_name):

        return self.shellting_index.get(shellting_name)

    def get_shellting_names(self):

        return self.shellting_index.keys()
