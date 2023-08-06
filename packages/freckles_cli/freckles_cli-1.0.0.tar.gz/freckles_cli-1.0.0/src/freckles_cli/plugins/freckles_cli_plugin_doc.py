# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import inspect

from omegaconf import OmegaConf

from freckles.frecklet.vars import VAR_ADAPTERS
from frutils.doc import Doc
from frutils.jinja2_filters import (
    ALL_FRUTIL_FILTERS,
    ALL_DEFAULT_JINJA2_FILTERS,
    ALL_FILTERS,
)

import logging
import sys
from collections import OrderedDict

import click
from ruamel.yaml import YAML

from freckles.defaults import FRECKLET_KEY_NAME
from freckles.frecklet.describe import (
    create_auto_vars,
    describe_frecklet,
    print_task_descriptions,
)
from freckles.frecklet.vars import VarsInventory
from freckles.utils.utils import print_multi_column_table
from freckles_cli.freckles_base_cli import handle_exception
from frkl import VarsType
from frutils import dict_merge, readable_yaml, reindent, special_dict_to_dict
from frutils.frutils_cli import output
from frutils.tasks.callback import get_all_callback_classes, get_callback_doc

yaml = YAML(typ="safe")

log = logging.getLogger("freckles")


def ignore_representer(representer, data):

    return representer.represent_scalar(u"!gnored", "skipped")


@click.group()
@click.pass_context
def doc(ctx):
    """
    Documentation to support developing with freckles.
    """

    pass


@doc.command("config", short_help="Documentation for config keys")
@click.option(
    "--limit-interpreters",
    "-l",
    help="only display interpreter data for interpreters that contain this string",
)
@click.argument("key", required=False, nargs=1)
@click.pass_context
def config_doc(ctx, key, limit_interpreters):
    """
    Display documentation for configuration keys.
    """

    # output_format = "yaml"
    context = ctx.obj["context"]

    click.echo()

    cnf = context._config.cnf

    for c_name in cnf.get_interpreter_names():
        if limit_interpreters and limit_interpreters not in c_name:
            continue

        interpreter = cnf.get_interpreter(c_name)
        # interpreter_type = interpreter_details["type"]

        matches = []
        for c_key in sorted(interpreter.schema.keys()):

            if key and key not in c_key:
                continue

            matches.append(c_key)

        if key and matches or not key:
            click.secho("{}".format(c_name), bold=True)
            click.echo()
        else:
            continue

        schema = interpreter.schema

        if not key and not schema:
            click.echo("  No config schema")
            click.echo()
            continue

        for c_key in matches:
            doc = interpreter.get_doc_for_key(c_key)
            click.secho(" {} ".format(c_key), bold=True, nl=False)
            key_schema = interpreter.get_schema_for_key(c_key)
            value_type = key_schema.get("type", "unknown_type")
            default = key_schema.get("default", None)
            if default is not None:
                if isinstance(default, bool):
                    default_str = "true" if default else "false"
                else:
                    default_str = str(default)
                click.echo("({}, default: {})".format(value_type, default_str))
            else:
                click.echo("({})".format(value_type))
            click.echo("    {}".format(doc.get_short_help()))

        click.echo()


@doc.command("filters")
@click.option(
    "--collection",
    "-c",
    help="which set of filters to display",
    type=click.Choice(["freckles", "jinja", "all"]),
    default="freckles",
)
@click.argument("filters", type=str, nargs=-1, required=False)
@click.option(
    "--show-help",
    "-h",
    help="display filter help",
    is_flag=True,
    type=bool,
    default=False,
)
@click.pass_context
def filters(ctx, collection, filters, show_help):
    """
    List all available template filters.

    The filters to filter filters are applied using 'and', which means only filters that match all of them will be displayed.
    """

    if collection == "freckles":
        filter_col = ALL_FRUTIL_FILTERS
    elif collection == "jinja":
        filter_col = ALL_DEFAULT_JINJA2_FILTERS
    else:
        filter_col = ALL_FILTERS

    if not filters:
        filter_filters = []
    else:
        filter_filters = list(filters)

    for filter_name, filter in sorted(filter_col.items()):

        help = filter["doc"].get_help(use_short_help=True, default="n/a")

        if filter_filters:
            match = True
            for ff in filter_filters:
                if show_help:
                    if ff not in filter_name and ff not in help:
                        match = False
                        break
                else:
                    if ff not in filter_name:
                        match = False
                        break
            if not match:
                continue

        click.secho(filter_name, bold=True)
        if show_help:
            click.echo()
            click.echo(reindent(help, 4))
            click.echo()


@doc.command("filter")
@click.argument("filter", nargs=1, required=True)
@click.pass_context
def filter(ctx, filter):
    """
    Display filter details.
    """

    click.echo()
    filter_col = ALL_FILTERS

    for filter_name, filter_d in sorted(filter_col.items()):

        help = filter_d["doc"].get_help(use_short_help=True, default="n/a")

        if filter in filter_name:

            click.secho(filter_name, bold=True)
            click.echo()
            click.echo(reindent(help, 4))
            click.echo()


def get_all_var_adapters():

    result = OrderedDict()
    for var_adapter_name, var_adapter in sorted(VAR_ADAPTERS.items()):

        help = var_adapter.__doc__
        if not help:
            help = "n/a"
        help = inspect.cleandoc(help)

        doc = Doc({"help": help})

        result[var_adapter_name] = doc

    return result


@doc.command("var-adapters")
@click.argument("filters", nargs=-1, required=False)
@click.option(
    "--show-help",
    "-h",
    help="display var-adapter help",
    is_flag=True,
    type=bool,
    default=False,
)
@click.pass_context
def var_adapters(ctx, filters, show_help):
    """
    List available var-adapters.
    """

    click.echo()
    if not filters:
        var_adapter_filters = []
    else:
        var_adapter_filters = list(filters)

    for var_adapter_name, var_adapter in get_all_var_adapters().items():

        help = var_adapter.get_help(use_short_help=True, default="n/a")

        if var_adapter_filters:
            match = True
            for ff in var_adapter_filters:
                if show_help:
                    if ff not in var_adapter_name and ff not in help:
                        match = False
                        break
                else:
                    if ff not in var_adapter_name:
                        match = False
                        break
            if not match:
                continue

        click.secho(var_adapter_name, bold=True)
        if show_help:
            click.echo()
            click.echo(reindent(help, 4))
            click.echo()


@doc.command("var-adapter")
@click.argument("var_adapter", nargs=1, required=True)
@click.pass_context
def var_adapter(ctx, var_adapter):
    """
    Display var-adapter details.
    """

    for var_adapter_name, var_adapter_d in get_all_var_adapters().items():

        help = var_adapter_d.get_help(use_short_help=True, default="n/a")

        if var_adapter in var_adapter_name:
            click.secho(var_adapter_name, bold=True)
            click.echo()
            click.echo(reindent(help, 4))
            click.echo()


@doc.command("callbacks")
@click.argument("filters", nargs=-1, required=False)
@click.option(
    "--show-help",
    "-h",
    help="display var-adapter help",
    is_flag=True,
    type=bool,
    default=False,
)
@click.pass_context
def callbacks(ctx, filters, show_help):
    """
    List available var-adapters.
    """

    click.echo()

    if not filters:
        callback_filters = []
    else:
        callback_filters = list(filters)

    for callback_name, callback_class in sorted(get_all_callback_classes().items()):

        doc = get_callback_doc(callback_class)
        help = doc.get_help(use_short_help=True, default="n/a")

        if callback_filters:
            match = True
            for ff in callback_filters:
                if show_help:
                    if ff not in callback_name and ff not in help:
                        match = False
                        break
                else:
                    if ff not in callback_name:
                        match = False
                        break
            if not match:
                continue

        click.secho(callback_name, bold=True)
        if show_help:
            click.echo()
            click.echo(reindent(help, 4))
            click.echo()


@doc.command("callback")
@click.argument("callback", nargs=1, required=True)
@click.pass_context
def callback(ctx, callback):
    """
    Display var-adapter details.
    """

    click.echo()
    for callback_name, callback_class in get_all_callback_classes().items():

        doc = get_callback_doc(callback_class)
        help = doc.get_help(use_short_help=True, default="n/a")

        if callback in callback_name:
            click.secho(callback_name, bold=True)
            click.echo()
            click.echo(reindent(help, 4))
            click.echo()


@doc.command("task-tree")
@click.argument("frecklet_name", nargs=1)
@click.pass_context
def task_tree(ctx, frecklet_name):
    """Print execution plan for a frecklet.

    Print out a hierarchical tree-structure, containing all tasks that will be executed, including their parents.
    """

    context = ctx.obj["context"]

    f, internal_name = context.load_frecklet(frecklet_name)
    click.echo()
    click.echo(
        "{} ({}):".format(frecklet_name, f.doc.get_short_help(list_item_format=True))
    )

    for n in f.task_tree.all_nodes():
        level = f.task_tree.level(n.identifier)
        if level == 0:
            continue
        padding = "  " * level
        # print(n.data["task"].keys())
        task = n.data["task"]
        name = task[FRECKLET_KEY_NAME]["name"]
        # import pp
        # pp(task)
        f_type = task[FRECKLET_KEY_NAME].get("type", "frecklet")
        short_help = ""
        if f_type == "frecklet":
            short_help = context.get_frecklet(name).doc.get_short_help(
                list_item_format=True
            )
            # short_help = task[FRECKLET_KEY_NAME].get("msg", None)
            title = "{} ({})".format(name, short_help)

        else:
            title = "{}::{}".format(f_type, name)
        print("{}- {}".format(padding, title))


@doc.command("task-list")
@click.argument("frecklet_name", type=str, nargs=1)
@click.argument("vars", type=VarsType(), nargs=-1)
@click.option(
    "--auto-vars",
    "-a",
    help="auto generate missing required variables",
    required=False,
    is_flag=True,
)
@click.pass_context
def task_list(ctx, frecklet_name, vars, auto_vars):
    """Print rendered tasklist for a frecklet.

    Render and process the frecklet task-list using the provided vars, display the output in human-readable form.

    """

    context = ctx.obj["context"]

    frecklet, internal_name = context.load_frecklet(frecklet_name)
    fx = frecklet.create_frecklecutable(context=context)

    if vars:
        var_all = special_dict_to_dict(OmegaConf.merge(*vars))
    else:
        var_all = {}

    if auto_vars:
        params = fx.frecklet.vars
        auto_vars = create_auto_vars(
            params, existing_vars=var_all, frecklet=fx.frecklet
        )
        click.echo("\n----------------------------------------------")
        click.echo("Auto-generated (missing) required variables:\n")
        output(auto_vars, output_type="yaml", indent=2)
        click.echo("----------------------------------------------\n")

        var_all = dict_merge(auto_vars, var_all, copy_dct=True)

    inv = VarsInventory(var_all)
    run_inv, _ = fx.create_run_inventory(inventory=inv)
    tasks = fx.process_tasks(inventory=run_inv)

    tl_string = readable_yaml(tasks, ignore_aliases=True)
    click.echo(tl_string)


@doc.command("frecklet")
@click.option(
    "--exploded", "-e", help="print exploded form", is_flag=True, default=False
)
@click.argument("frecklet_name", type=str, nargs=1)
@click.pass_context
def print_frecklet(ctx, frecklet_name, exploded):
    """Print frecklet content."""

    context = ctx.obj["context"]
    frecklet, internal_name = context.load_frecklet(frecklet_name)

    if not frecklet:
        click.echo("No frecklet with name: {}".format(frecklet_name))
        sys.exit(1)

    if not exploded:
        result = frecklet.pretty_print

        click.echo()
        click.echo(result)
        click.echo()
    else:
        result = frecklet.exploded

        click.echo()
        for k, v in result.items():
            click.secho(k + ":", bold=True)
            click.echo()
            details = readable_yaml(v, indent=2, ignore_aliases=True)
            click.echo(details)


# @frecklet.command("raw")
# @click.argument("frecklet_name", type=str, nargs=1)
# @click.pass_context
# def raw_frecklet(ctx, frecklet_name):
#     """Print the raw frecklet content."""
#
#     context = ctx.obj["context"]
#     frecklet, internal_name = context.load_frecklet(frecklet_name)
#
#     if not frecklet:
#         click.echo("No frecklet with name: {}".format(frecklet_name))
#         sys.exit(1)
#
#     result = frecklet.ting_content
#
#     click.echo()
#     click.echo(result)
#     click.echo()


@doc.command("frecklet-path")
@click.argument("frecklet_name", type=str, nargs=1)
@click.pass_context
def path_frecklet(ctx, frecklet_name):
    """Print absolute path to frecklet."""

    context = ctx.obj["context"]
    frecklet, internal_name = context.load_frecklet(frecklet_name, validate=True)

    if not frecklet:
        click.echo("No frecklet with name: {}".format(frecklet_name))
        sys.exit(1)

    click.echo()
    if not hasattr(frecklet, "full_path"):
        click.echo(
            "frecklet '{}' does not have a 'path' attribute, probably dynamically created...".format(
                frecklet_name
            )
        )
    else:
        click.echo(frecklet.full_path)
    click.echo()


def print_args_doc(frecklet, full=False, sort_by_name=False):

    if full:
        result = OrderedDict()
        if sort_by_name:
            for k, arg in frecklet.vars.items():
                details = arg.pretty_print_dict()
                result[k] = details
        else:
            for k, arg in frecklet.vars.items():
                if arg.required is True:
                    details = arg.pretty_print_dict()
                    result[k] = details
            for k, arg in frecklet.vars.items():
                if arg.required is False:
                    details = arg.pretty_print_dict()
                    result[k] = details

        click.echo()

        for k, v in result.items():
            click.secho(k, bold=True)
            click.echo()
            details = readable_yaml(v, indent=2, ignore_aliases=True)
            click.echo(details)

    else:

        data = OrderedDict()
        if sort_by_name:
            for k, arg in frecklet.vars.items():
                data[k] = arg
        else:
            for k, arg in frecklet.vars.items():
                if arg.required is True:
                    data[k] = arg
            for k, arg in frecklet.vars.items():
                if arg.required is False:
                    data[k] = arg

        result = []
        for k, arg in data.items():
            if arg.required:
                arg_req = "X"
            else:
                arg_req = ""

            desc = arg.doc.get_short_help(list_item_format=True, use_help=True)
            arg_type = arg.type
            if arg.default is not None:
                arg_default = arg.default
            else:
                arg_default = ""
            result.append([k, arg_type, arg_req, arg_default, desc])

        click.echo()

        print_multi_column_table(result, ["arg", "type", "req", "default", "desc"])


@doc.command("args")
@click.option(
    "--full", "-f", is_flag=True, help="Print the full description for every argument."
)
@click.argument("frecklet_name", type=str, nargs=1)
@click.pass_context
def args(ctx, frecklet_name, full, raw=False, sort_by_name=False):
    """Print arguments of a frecklets."""

    context = ctx.obj["context"]
    frecklet, internal_name = context.load_frecklet(frecklet_name)

    if not frecklet:
        click.echo("No frecklet with name: {}".format(frecklet_name))
        sys.exit(1)

    try:

        if raw:

            if frecklet._metadata.get("args", None):
                click.echo("{}:".format("args"))
                result = readable_yaml(
                    frecklet._metadata["args"], sort_keys=True, ignore_aliases=True
                )
                click.echo(reindent(result, 2))

        else:

            print_args_doc(frecklet=frecklet, full=full, sort_by_name=sort_by_name)
    except (Exception) as e:
        handle_exception(e)


@doc.command("describe")
@click.argument("frecklet_name", type=str, nargs=1)
@click.argument("vars", type=VarsType(), nargs=-1)
@click.option(
    "--auto-vars",
    "-a",
    help="auto generate missing required variables",
    required=False,
    is_flag=True,
)
@click.pass_context
def describe(ctx, frecklet_name, vars, auto_vars):
    """Print task execution details for frecklet.

    Render and process the frecklet task-list using the provided vars, display the output in human-readable form.
    """

    try:
        context = ctx.obj["context"]
        frecklet, _ = context.load_frecklet(frecklet_name)
        if vars:
            vars = special_dict_to_dict(OmegaConf.merge(*vars))
        else:
            vars = {}
        tasks_descs, auto_vars_dict = describe_frecklet(
            context=context, frecklet=frecklet, vars=vars, auto_vars=auto_vars
        )

        if auto_vars_dict:
            click.echo("\n----------------------------------------------")
            click.echo("Auto-generated (missing) required variables:\n")
            output(auto_vars_dict, output_type="yaml", indent=2)
            click.echo("----------------------------------------------\n")

        click.echo()
        print_task_descriptions(tasks_descs)
    except (Exception) as e:
        handle_exception(e)


@doc.command()
@click.argument("frecklet_name", nargs=1)
@click.argument("attributes", metavar="ATTRIBUTE", nargs=-1)
@click.option(
    "--attribute-names", "-n", is_flag=True, help="list names of all attributes"
)
@click.pass_context
def attributes(ctx, frecklet_name, attributes, attribute_names):
    """Prints attributes of a frecklet (for debug)."""

    context = ctx.obj["context"]

    f, internal_name = context.load_frecklet(frecklet_name)

    click.echo()

    if attribute_names:
        for n in f._ting_attribute_names:
            click.echo(n)
        click.echo()
        sys.exit()

    if not attributes:
        attributes = f._ting_attribute_names

    result = OrderedDict()
    not_available = []
    for a in sorted(attributes):

        if not hasattr(f, a):
            not_available.append(a)
        else:
            result[a] = getattr(f, a)

    if not_available:
        click.echo()
        click.echo(
            "Attribute(s) not available for frecklet '{}':".format(frecklet_name)
        )
        for a in not_available:
            click.echo("  - {}".format(a))
        click.echo()
        sys.exit(1)

    # r = {Arg: arg_representer, Argument: ignore_representer, Option: ignore_representer, Doc: ignore_representer, Tree: ignore_representer}
    r = {}
    for k, v in result.items():
        click.secho(k, bold=True)
        click.echo()
        try:
            output(
                v,
                output_type="yaml",
                yaml_representers=r,
                indent=4,
                ignore_aliases=True,
                sort_keys=True,
            )
        except (Exception):
            output(v, output_type="pformat", indent=4)
        click.echo()
