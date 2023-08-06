# -*- coding: utf-8 -*-
import logging
import sys

import click
import colorama
from stevedore.extension import ExtensionManager

from frutils.frutils_cli import logzero_option
from ..freckles_base_cli import FrecklesBaseCommand


colorama.init()

VARS_HELP = "variables to be used for templating, can be overridden by cli options if applicable"
DEFAULTS_HELP = "default variables, can be used instead (or in addition) to user input via command-line parameters"
KEEP_METADATA_HELP = "keep metadata in result directory, mostly useful for debugging"
FRECKLECUTE_EPILOG_TEXT = "freckles is free to use in combination with open source software, for information on private licenses visit: https://freckles.io"

log = logging.getLogger("freckles")


# extensions
# ------------------------------------------------------------------------
def load_plugins():
    """Loading a dictlet finder extension.

    Returns:
      ExtensionManager: the extension manager holding the extensions
    """

    log2 = logging.getLogger("stevedore")
    out_hdlr = logging.StreamHandler(sys.stderr)
    out_hdlr.setFormatter(logging.Formatter("freckles plugin error -> %(message)s"))
    out_hdlr.setLevel(logging.DEBUG)
    log2.addHandler(out_hdlr)
    log2.setLevel(logging.INFO)

    log.debug("Loading freckles plugin...")

    mgr = ExtensionManager(
        namespace="freckles_cli.plugins",
        invoke_on_load=False,
        propagate_map_exceptions=True,
    )

    return mgr


class FrecklesCommand(FrecklesBaseCommand):
    def __init__(self, *args, **kwargs):

        super(FrecklesCommand, self).__init__(invoke_without_command=False, **kwargs)
        self.plugins = load_plugins()
        self.commands = {}
        for plugin in self.plugins:
            name = plugin.name
            ep = plugin.entry_point
            command = ep.load()
            self.commands[name] = command

    def list_freckles_commands(self, ctx):

        return sorted(self.commands.keys())

    def get_freckles_command(self, ctx, name, **kwargs):

        # ctx.obj["control_dict"] = self.control_dict
        ctx.obj["run_config"] = self.run_config
        ctx.obj["extra_vars"] = self.extra_vars
        ctx.obj["dump_frecklet"] = self.dump_frecklet

        command = self.commands.get(name, None)

        if command:
            return command

        return None


@click.command(
    name="freckles",
    cls=FrecklesCommand,
    epilog=FRECKLECUTE_EPILOG_TEXT,
    subcommand_metavar="PLUGIN",
)
# @click.option("--vars", "-v", help="additional vars", multiple=True, type=VarsType())
@logzero_option()
@click.pass_context
def cli(ctx, vars, **kwargs):
    """The 'freckles' command-line tool is the central application in the freckles package.

    It allows users to configure the application itself, manage contexts and adapters, list
    available frecklets and their details, and, most importantly, run and debug those frecklets.

    The freckles package provides other applications (most notably: frecklecute) that allow to
    do some of those tasks in easier ways, but in a pinch users could do without those, as long
    as the 'freckles' commmand-line app is available.

    """
    pass


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover

if getattr(sys, "frozen", False):
    cli(sys.argv[1:])
