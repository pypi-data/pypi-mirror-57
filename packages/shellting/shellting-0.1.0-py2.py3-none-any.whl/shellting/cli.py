# -*- coding: utf-8 -*-

"""Console script for tempting."""
import logging
import sys

import click
import click_log
from click import MultiCommand

from frutils.config import Cnf
from . import print_version
from .shellting import ShelltingContext

log = logging.getLogger("freckles")
click_log.basic_config(log)


def path_callback(ctx, param, value):

    if ctx.obj is None:
        ctx.obj = {}
    ctx.obj["path"] = value


def jinja_env_callback(ctx, param, value):

    if ctx.obj is None:
        ctx.obj = {}
    ctx.obj["jinja_env"] = value


def set_vars(ctx, param, value):

    if ctx.obj is None:
        ctx.obj = {}
    ctx.obj["vars"] = value


def set_repos(ctx, param, value):
    if ctx.obj is None:
        ctx.obj = {}
    ctx.obj["repos"] = value


class ShelltingMultiCommand(MultiCommand):
    def __init__(
        self,
        print_version_callback=print_version,
        name=None,
        invoke_without_command=False,
        no_args_is_help=None,
        subcommand_metavar=None,
        chain=False,
        result_callback=None,
        **kwargs
    ):

        super(ShelltingMultiCommand, self).__init__(
            name=name,
            invoke_without_command=invoke_without_command,
            no_args_is_help=no_args_is_help,
            subcommand_metavar=subcommand_metavar,
            chain=chain,
            result_callback=result_callback,
            **kwargs
        )
        self.print_version_callback = print_version_callback
        self.path = None
        self.show_vars = False
        self.index = None
        self.index_cache = {}

        self.cnf = Cnf()
        self.shellting_context = None

    def init_shellting_context(self, ctx):

        if self.shellting_context is not None:
            return

        repos = ctx.obj["repos"]
        self.shellting_context = ShelltingContext("default", self.cnf, repos=repos)

    def list_commands(self, ctx):

        self.init_shellting_context(ctx)

        return self.shellting_context.get_shellting_names()

    def create_alias_map(self, arg_map):

        alias_map = {}

        for arg_name, arg in arg_map.items():
            if "param_decls" not in arg.get("cli", {}).keys():
                continue

            for a in arg["cli"]["param_decls"]:
                if a == arg_name:
                    continue
                if a in alias_map.keys():
                    raise Exception(self, "Duplicate alias/key: {}".format(a))
                if "/" in a:
                    a = a.split("/")[0]
                a = a.strip("-")
                a = a.replace("-", "_")
                alias_map[a] = arg_name

        return alias_map

    def translate_cli_args(self, cli_vars, arg_map):

        alias_map = self.create_alias_map(arg_map)

        result = {}

        for key, value in cli_vars.items():
            if value is None:
                continue

            if isinstance(value, bool):
                value = "true" if value else "false"

            if key in alias_map.keys():
                result[alias_map[key]] = value
            else:
                result[key] = value

        return result

    def get_command(self, ctx, cmd_name):

        self.init_shellting_context(ctx)

        shellting = self.shellting_context.get_shellting(cmd_name)

        @click.command(name=cmd_name)
        def command(*args, **kwargs):

            user_input = self.translate_cli_args(kwargs, shellting.args)
            src = self.shellting_context.render_script(cmd_name, args=user_input)

            click.echo(src)

        # print(ctx.params)
        details = True
        if details:
            try:
                cli_args = shellting.cli_args
            except (Exception) as e:
                log.warning("Error parsing tempting '{}': {}".format(cmd_name, e))
                log.debug(e, exc_info=1)
                return None
        else:
            cli_args = []

        command.params = cli_args
        command.help = shellting.doc.get_help()
        command.short_help = shellting.doc.get_short_help(list_item_format=True)

        return command


@click.command(
    name="shellting", cls=ShelltingMultiCommand, subcommand_metavar="SHELLTING"
)
@click.option(
    "--write",
    "-w",
    help="write rendered shellting to file",
    multiple=False,
    required=False,
    type=str,
    metavar="PATH",
)
@click.option(
    "--force",
    "-f",
    help="overwrite existing file",
    required=False,
    default=False,
    is_flag=True,
)
@click.option(
    "--repo",
    "-r",
    help="additional repo(s) to use",
    multiple=True,
    callback=set_repos,
    is_eager=True,
    expose_value=True,
    default=[],
)
@click_log.simple_verbosity_option(logging.getLogger(), "--verbosity")
@click.pass_context
def cli(ctx, **kwargs):
    """Shell script argument augmenter.
    """

    pass


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
