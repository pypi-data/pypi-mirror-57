# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import os
import sys

import click
from cursor import cursor
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

from freckles.context.config import is_unlocked
from freckles.defaults import FRECKLES_CONFIG_DIR
from freckles_cli.freckles_base_cli import handle_exception
from frutils import readable, unsorted_to_sorted_dict
from frutils.frutils_cli import output

yaml = YAML()


def fail_if_locked():

    locked = not is_unlocked()
    if locked:
        click.echo(
            "\nThe initial freckles configuration is locked. Use the following command to unlock:\n\nfreckles context unlock\n\nFor more information, please visit: https://freckles.io/doc/configuration"
        )
        sys.exit(1)


@click.group()
@click.pass_context
def context(ctx):
    """'context'-related tasks.

    A context is a set of configuration options that control which frecklets are available for execution, and
    the way in which they will be executed.

    Contexts are stored in (yaml-format) text files under ~/.config/freckles with a '.context' file extension. The context
    name is the filename (without extension). This subset of commands lets you display, edit & create those context files.
    You can do all that with just a text-editor though, if you prefer.

    By default, the freckles configuration is locked, in order to not have some of the more advanced options that could
    potentially affect security disabled. To unlock the configuration, issue:

        freckles context unlock

    For more information on contexts, visit https://freckles.io/dec/configuration.
    """

    pass


@context.command(
    "export", short_help="export frecklets & resources of the current context"
)
@click.option(
    "--delete-before-copy",
    "-d",
    help="delete destination before copy",
    default=False,
    is_flag=True,
)
@click.option(
    "--ignore-errors", "-i", help="ignore any errors", default=False, is_flag=True
)
@click.argument("target", nargs=1)
@click.pass_context
def export(ctx, target, delete_before_copy, ignore_errors):
    """Export frecklets & resources of the current context.
    """

    context = ctx.obj["context"]

    try:
        cursor.hide()
        context.export(
            target,
            delete_destination_before_copy=delete_before_copy,
            ignore_errors=ignore_errors,
        )
    except (Exception) as e:
        handle_exception(e)
    finally:
        cursor.show()


@context.command("show", short_help="print current configuration")
@click.option("--show-interpreters", "-i", help="show interpreted data", is_flag=True)
@click.option(
    "--limit-interpreters",
    "-l",
    help="only display interpreter data for interpreters that contain this string (implies '--show-interpreters')",
)
@click.pass_context
def show_current(ctx, show_interpreters, limit_interpreters):
    """Print the current configuration, including documentation (optional).

    This will print the global configuration key/value pairs, as well as the interpreted ones for each added
    configuration interperter.
    """
    output_format = "yaml"

    context = ctx.obj["context"]
    run_config = ctx.obj["run_config"]

    cnf = context._config.cnf

    config_values = cnf.config
    indent = 0
    if limit_interpreters:
        show_interpreters = True
    if show_interpreters:
        indent = 2
    config_values_string = readable(
        unsorted_to_sorted_dict(config_values), out=output_format, indent=indent
    )

    click.echo()
    if show_interpreters:
        click.secho("Configuration", bold=True)
        click.secho("-------------", bold=True)
        click.echo()

    click.echo(config_values_string)
    click.echo()

    if not show_interpreters:
        sys.exit()

    click.secho("Interpreters", bold=True)
    click.secho("------------", bold=True)
    click.echo()

    for c_name in cnf.get_interpreter_names():

        interpreter = cnf.get_interpreter(c_name)

        if limit_interpreters and limit_interpreters not in c_name:
            continue

        title = c_name
        click.secho("  {}".format(title), bold=True)
        click.echo()

        validated = interpreter.overlay(run_config)

        if not validated:
            click.echo("    No configuration.")
            click.echo()
            continue

        details = CommentedMap()

        for k, schema in sorted(interpreter.schema.items()):
            v = validated.get(k, None)
            full = interpreter.get_doc_for_key(k)
            short_help = full.get_short_help()
            details[k] = CommentedMap()
            details[k]["desc"] = short_help
            if v is None:
                v = "n/a"
            details[k]["current value"] = v
            details[k]["default"] = schema.get("default", "n/a")

        for k, v in details.items():
            if details:
                click.secho("    {}:".format(k), bold=True)
                temp = readable(v, out=output_format, indent=6)
                click.echo(temp.rstrip())

        click.echo()

    # click.echo()


@context.command("copy", short_help="copy current configuration to new context")
@click.argument("context_name", nargs=1)
@click.option(
    "--edit",
    "-e",
    is_flag=True,
    default=False,
    help="open new context configuration in editor after copying",
)
@click.option(
    "--force",
    "-f",
    is_flag=True,
    default=False,
    help="overwrite context configuration if already exists",
)
@click.pass_context
def copy_context(ctx, context_name, edit, force):
    """Copies the current configuration into a new context configuration file.

    The context configuration files are YAML text files which are stored under $HOME/.config/freckles with a '.context'
    filename extension. This command copies all values that are set, as well as defaults.
    """

    fail_if_locked()
    cnf = ctx.obj["context"]._config.cnf

    target = os.path.join(FRECKLES_CONFIG_DIR, "{}.context".format(context_name))
    try:
        cnf.save_current(target, force=force)
    except (Exception) as e:
        click.echo(e)
        sys.exit()

    if edit:
        click.edit(filename=target)


@context.command("delete", short_help="delete configuration profile")
@click.argument("profile_name", metavar="PROFILE_NAME", nargs=1)
@click.pass_context
def delete_profile(ctx, profile_name):
    """Deletes a context configuration.

    The configuration file is located under $HOME/.config/freckles (or $HOME/.freckles)
    """

    fail_if_locked()

    file = os.path.join(FRECKLES_CONFIG_DIR, "{}.context".format(profile_name))

    if os.path.exists(file):
        os.remove(file)


@context.command("edit", short_help="edit a context configuration")
@click.argument("profile_name", metavar="PROFILE_NAME", nargs=1, default="default")
@click.pass_context
def edit_profile(ctx, profile_name):
    """Edits a context configuration with the default editor.

    """

    fail_if_locked()

    path = os.path.join(FRECKLES_CONFIG_DIR, "{}.context".format(profile_name))
    click.edit(filename=path)


@context.command("list", short_help="list all available contexts")
@click.option(
    "--details", "-d", help="show contents of each context profile", is_flag=True
)
@click.pass_context
def list_contexts(ctx, details):
    """Lists all available context configurations."""

    freckles = ctx.obj["freckles"]

    click.echo()
    for context_name in sorted(freckles._context_configs.keys()):
        context = freckles._context_configs[context_name]
        if not details:
            print(context_name)
            continue

        click.secho(context_name, bold=True)
        click.echo()
        output(context.config_dict, output_type="yaml", sort_keys=True)
        click.echo()

    click.echo()
