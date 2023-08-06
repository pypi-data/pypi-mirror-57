# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import logging
import sys
from collections import OrderedDict

import click
from colorama import Style
from ruamel.yaml import YAML

from freckles.utils.utils import print_frecklet_list
from freckles_cli.plugins.freckles_cli_plugin_doc import print_args_doc

yaml = YAML(typ="safe")

log = logging.getLogger("freckles")


def print_frecklet_details(frecklet, path=True, args=False):

    click.echo()
    click.secho(frecklet.id, bold=True)
    click.secho("=" * len(frecklet.id), bold=True)
    details = []
    if path:
        details.append("full_path")

    result = OrderedDict()

    for d in details:
        if hasattr(frecklet, d):
            temp = getattr(frecklet, d)
        else:
            temp = "n/a"
        result[Style.BRIGHT + d + Style.RESET_ALL] = Style.DIM + temp + Style.RESET_ALL

    if result:
        click.echo()
    for k, v in result.items():
        click.echo(k + ": " + v)

    if args:
        click.echo()
        print_args_doc(frecklet=frecklet, full=False, sort_by_name=False)
    click.echo()


@click.command()
@click.argument("filter", type=str, nargs=-1, required=False)
@click.option(
    "--args",
    "-a",
    help="display frecklet argument documentation",
    type=bool,
    is_flag=True,
)
@click.option(
    "--details", "-d", help="display frecklet details", type=bool, is_flag=True
)
@click.pass_context
def list(ctx, filter, details, args):
    """
    List available frecklets and their details.
    """

    context = ctx.obj["context"]

    apropos = filter
    check_doc = False

    result = OrderedDict()
    for f_name, f in context.frecklet_index.items():
        match = True
        for a in apropos:
            if a not in f_name:
                match = False
                break

        if match:
            result[f_name] = f
            continue

        if check_doc:
            match = f.doc.matches_apropos(apropos, only_short_help=True)
        else:
            match = False

        if match:
            result[f_name] = f

    if not details and not args:
        print_frecklet_list(result)
    else:
        for f_n, f in result.items():
            print_frecklet_details(f, path=details, args=args)

    sys.exit(0)
