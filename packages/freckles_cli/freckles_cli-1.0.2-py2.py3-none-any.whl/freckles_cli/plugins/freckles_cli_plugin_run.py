# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import copy
import logging
import os

import click
from ruamel.yaml import YAML

from freckles_cli.freckles_base_cli import handle_exception, run_frecklet
from pyckles.codegen import PycklesCodegen
from pyckles.contexts.python import PythonCachedContext

yaml = YAML(typ="safe")

log = logging.getLogger("freckles")

TEST_INVENTORY = {
    "target": "localhost",
    "gid": 3000,
    "group": "testgroup",
    "system_user": False,
    "name": "Markus",
    "path": "/tmp/markus",
}


def run_python(ctx, path):

    context = ctx.obj["context"]
    pcc = PythonCachedContext(context)
    template_name = "python_3_src.j2"
    package_name = "pycklets"

    codegen = PycklesCodegen(context, template_name=template_name)
    module = codegen.generate_pycklets_package(package_name=package_name)

    module.run_frecklets = pcc.run_frecklets
    module.run_pycklets = pcc.run_pycklets

    with open(path, "r", encoding="utf-8") as py_file:
        content = py_file.read()

    c = compile(content, filename=path, mode="exec")

    try:
        exec(c)
    except (Exception) as e:
        handle_exception(e)


def run_frecklet_data_or_path(ctx, frecklet):

    context = ctx.obj["context"]
    extra_vars = ctx.obj["extra_vars"]
    run_config = ctx.obj["run_config"]
    dump_frecklet = ctx.obj["dump_frecklet"]

    try:
        f, frecklet_name = context.load_frecklet(frecklet, validate=True)

        vars = copy.deepcopy(extra_vars)

        run_frecklet(
            ctx=ctx,
            frecklet=f,
            freckles_context=context,
            run_config=run_config,
            vars=vars,
            dump_frecklet=dump_frecklet,
        )

    except (Exception) as e:
        handle_exception(e)


def run_from_stdin(ctx):

    frecklet_data = []

    log.debug("waiting for input from stdin...")
    stream = click.get_text_stream("stdin", encoding="utf-8")
    for line in stream:
        frecklet_data.append(line)

    frecklet_data = "".join(frecklet_data)

    freckles_context = ctx.obj["context"]
    run_config = ctx.obj["run_config"]
    extra_vars = ctx.obj["extra_vars"]

    try:

        frecklet, frecklet_name = freckles_context.load_frecklet(
            frecklet_data, validate=True
        )

        run_frecklet(
            ctx=ctx,
            frecklet=frecklet,
            freckles_context=freckles_context,
            run_config=run_config,
            vars=extra_vars,
            dump_frecklet=False,
        )
    except (Exception) as e:
        handle_exception(e)


@click.command()
# @click.option("--vars", "-v", help="vars for frecklet", multiple=True, type=VarsType())
@click.argument("frecklet", required=False, metavar="FRECKLET", nargs=1)
@click.pass_context
def run(ctx, frecklet):
    """
    Run instructions from a Python/JSON/YAML file, or from stdin.

    Depending on the specified 'frecklet' argument, different modes of executions are used:

      - if no 'frecklet' argument is provided, this command uses a string piped in via stdin as input

      - if the provided frecklet argument is a file where the filename ends with '.py', it will be executed using a Python interpreter

      - if the argument is the name of a frecklet in the current context, that frecklet will be executed

      - if the argument is the path to a file (that doesn't end with '.py'), that file is read and the content is interpreted as frecklet data

      - if the argument is a url, the url will be downloaded and the content is interpreted as frecklet data ('allow_remote' config option needs to be set to 'true')

    *Notes*

    stdin:

      Either pipe in your frecklet data ala:

          echo '[{"debug-var":{"var": "ansible_facts"}}]' | freckles run

      Or type it in manually after starting 'freckles read-stdin'. In the latter case, press Ctrl-d three times to indicate you are finished.
    """

    try:
        context = ctx.obj["context"]

        if frecklet:
            frecklet = frecklet.strip()

        run_type = None
        path = None

        if not frecklet:
            run_type = "stdin"
        elif (frecklet.startswith("{") and frecklet.endswith("}")) or (
            frecklet.startswith("[") and frecklet.endswith("]")
        ):
            run_type = "frecklet"
        elif frecklet in context.get_frecklet_names():
            run_type = "frecklet"
        else:
            path = os.path.abspath(os.path.expanduser(frecklet))

            if os.path.isfile(path):
                if path.endswith(".py"):
                    run_type = "python"

        if run_type is None:
            run_type = "frecklet"

        if run_type == "python":
            run_python(ctx, path)
        elif run_type == "frecklet":
            run_frecklet_data_or_path(ctx, frecklet)
        elif run_type == "stdin":
            run_from_stdin(ctx)
    except (Exception) as e:
        handle_exception(e)

    # if not frecklet_data:
    #     frecklet_data = []
    #
    #     stream = click.get_text_stream("stdin", encoding="utf-8")
    #
    #     for line in stream:
    #         frecklet_data.append(line)
    #
    #     frecklet_data = "".join(frecklet_data)
    #     frecklet_data = [frecklet_data]

    # context = ctx.obj["context"]
    #
    # all_vars = {}
    # for v in vars:
    #     dict_merge(all_vars, v, copy_dct=False)
    #
    # run_config = ctx.obj["run_config"]
    #
    # frecklets = []
    #
    # for fd in frecklet_data:
    #
    #     if fd in context.get_frecklet_names():
    #         frecklets.append(fd)
    #
    # import pp
    # pp(frecklets)

    # run_frecklet(
    #     ctx=ctx,
    #     frecklet_name=frecklet,
    #     freckles_context=freckles_context,
    #     run_config=run_config,
    #     vars=all_vars,
    # )
