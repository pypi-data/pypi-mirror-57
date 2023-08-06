# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import io
import json
import logging
import os
import sys
import time

import click
from ruamel.yaml import YAML

from freckles.utils.runs import (
    RunWatchManager,
    FrecklesRunsLogTerminalOutput,
    get_last_run,
    print_task_detail,
    FrecklesCurrentRunsWatcher,
)
from freckles_cli.freckles_base_cli import handle_exception
from frutils import output
from frutils.frutils_cli import CursorOff

yaml = YAML(typ="safe")

log = logging.getLogger("freckles")


@click.group(name="runs")
@click.pass_context
def runs(ctx):
    """
    Information about previous freckles run(s).
    """

    pass


@runs.command("current")
@click.option("--json", "-j", help="output in json format", is_flag=True)
# @click.option(
#     "--watch",
#     "-w",
#     help="keep running and watch for changes in freckles runs",
#     is_flag=True,
# )
# @click.option(
#     "--details",
#     "-d",
#     help="print run details",
#     is_flag=True
# )
def current(json):
    """print all currently running runs"""

    # details = False
    # current_runs = get_current_runs()
    #
    # if not json:
    #     for r in current_runs.values():
    #
    #         alias = r["run_alias"]
    #
    #         if not details:
    #             click.echo(alias)
    # else:
    #     result = []
    #     for r in current_runs.values():
    #         result.append(r)
    #
    #     output(result, output_type="json")
    with CursorOff():
        click.echo("\nStarting to monitor current freckles jobs...\n")

        watcher = FrecklesCurrentRunsWatcher()
        rw = RunWatchManager(watcher)
        rw.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            rw.stop()

        rw.join_runs_watch()


@runs.command("current-logs")
@click.option(
    "--adapter-log",
    "-a",
    help="display/watch adapter-specific log (if it exists)",
    is_flag=True,
)
def current_logs(adapter_log):
    """watch logs of currently running jobs"""

    with CursorOff():
        try:
            click.echo("\nStarting to monitor current freckles job logs...\n")

            watcher = FrecklesRunsLogTerminalOutput(adapter_log=adapter_log)

            rw = RunWatchManager(watcher)

            rw.start()
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                rw.stop()

            rw.join_runs_watch()
        except (Exception) as e:
            handle_exception(e)


@runs.command("last")
@click.option("--json", "-j", help="output in json format", is_flag=True)
def last(json):

    run_data = get_last_run()
    if run_data is None:
        click.echo(
            "No data for last run. Use the '-c keep_run_folder=true' command-line argument to save run information."
        )
        sys.exit()

    if not json:
        click.echo()
        output(run_data, output_type="yaml")
        click.echo()
    else:
        output(run_data, output_type="json")


@runs.command("last-log")
@click.option(
    "--adapter-log",
    "-a",
    help="display/watch adapter-specific log (if it exists)",
    is_flag=True,
)
def last_logs(adapter_log):

    run_data = get_last_run()
    if run_data is None:
        click.echo(
            "No data for last run. Use the '-c keep_run_folder=true' command-line argument to save run information."
        )
        sys.exit()

    env_dir = run_data["env_dir"]

    if adapter_log:
        adapter = run_data["adapter"]
        if adapter != "nsbl":
            click.echo("Native log display for adapter '{}' not supported.")
            sys.exit()
        log_file = os.path.join(env_dir, "nsbl/logs/ansible_run_log")
    else:
        log_file = os.path.join(env_dir, "run_log.json")

    if not os.path.isfile(log_file):
        click.echo("No log file: {}".format(log_file))
        sys.exit()

    with io.open(log_file, "r", encoding="utf-8") as f:
        content = f.read()

    if adapter_log:
        click.echo(content)
    else:
        click.echo()
        for line in content.split("\n"):
            if not line.strip():
                continue
            task_detail = json.loads(line)
            print_task_detail(task_detail["value"], alias=None)
        click.echo()


# @runs.command("path")
# @click.pass_context
# def path(ctx):
#
#     # output_format = "yaml"
#     context = ctx.obj["context"]
#     cnf = context.cnf.get_interpreter("adapter_run_config_nsbl")
#     last_run_folder = cnf.config.get("add_symlink_to_env")
#
#     click.echo()
#     click.echo(os.path.realpath(last_run_folder))
#
#
# @runs.command("info")
# @click.option("--play/--no--play", help="display play info", default=False)
# @click.option("--path/--no-path", help="display path info", default=False)
# @click.option("--config/--no-config", help="display ansible.cfg content", default=False)
# @click.option("--roles/--no-roles", help="display role(s) info", default=False)
# @click.option(
#     "--tasklists/--no-tasklists", help="display tasklists info", default=False
# )
# @click.option("--all", help="display all information", is_flag=True, default=False)
# @click.pass_context
# def info(ctx, play, path, config, roles, tasklists, all):
#     """prints details of the last run"""
#
#     # output_format = "yaml"
#
#     if all:
#         play = True
#         path = True
#         config = True
#         roles = True
#         tasklists = True
#
#     if not play and not path and not config and not roles and not tasklists:
#         path = True
#         play = True
#
#     click.echo()
#
#     context = ctx.obj["context"]
#     cnf = context.cnf.get_interpreter("adapter_run_config_nsbl")
#     last_run_folder = cnf.config.get("add_symlink_to_env")
#
#     base_folder = os.path.realpath(last_run_folder)
#     plays_folder = os.path.join(base_folder, "plays")
#     # inventory_folder = os.path.join(base_folder, "inventory")
#     roles_folder = os.path.join(base_folder, "roles")
#     tasklists_folder = os.path.join(base_folder, "task_lists")
#     # debug_folder = os.path.join(base_folder, "debug")
#
#     if path:
#         click.secho("path", bold=True)
#         click.echo()
#         click.echo("  base folder: {}".format(base_folder))
#         # click.echo("  plays: {}".format(plays_folder))
#         # click.echo("  inventory: {}".format(inventory_folder))
#         # click.echo("  roles: {}".format(roles_folder))
#         # click.echo("  tasklists: {}".format(tasklists_folder))
#         # click.echo("  debug: {}".format(debug_folder))
#         # click.echo("  run script: {}".format(os.path.join(base_folder, "run_all_plays.sh")))
#         # click.echo("  debug script: {}".format(os.path.join(debug_folder, "debug_all_plays.sh")))
#         click.echo()
#     if play:
#         click.secho("plays", bold=True)
#         click.echo()
#         plays = [x for x in os.listdir(plays_folder) if x.startswith("play_")]
#         for p in plays:
#             click.secho("  {}".format(p), bold=True)
#             click.echo("  ")
#             with io.open(os.path.join(plays_folder, p), encoding="utf-8") as f:
#                 content = f.read()
#             click.echo(reindent(content, 4))
#         click.echo()
#     if config:
#         click.secho("ansible.cfg", bold=True)
#         click.echo()
#         with io.open(os.path.join(plays_folder, "ansible.cfg"), encoding="utf-8") as f:
#             content = f.read()
#         click.echo(reindent(content, 2))
#         click.echo()
#     if roles:
#         click.secho("roles", bold=True)
#         click.echo()
#         if os.path.exists(os.path.join(roles_folder, "internal")):
#             internal = [
#                 x
#                 for x in os.listdir(os.path.join(roles_folder, "internal"))
#                 if os.path.isdir(os.path.join(roles_folder, "internal", x))
#             ]
#         else:
#             internal = []
#         if os.path.exists(os.path.join(roles_folder, "external")):
#             external = [
#                 x
#                 for x in os.listdir(os.path.join(roles_folder, "external"))
#                 if os.path.isdir(os.path.join(roles_folder, "external", x))
#             ]
#         else:
#             external = []
#         if internal:
#             click.secho("  internal", bold=True)
#             click.echo()
#             for i in internal:
#                 click.echo("    - {}".format(i))
#             click.echo()
#         if external:
#             click.secho("  external", bold=True)
#             click.echo()
#             for i in external:
#                 click.echo("    - {}".format(i))
#             click.echo()
#         if not internal and not external:
#             click.echo("    - no roles used.\n")
#     if tasklists:
#         click.secho("task lists", bold=True)
#         click.echo()
#         tasklists = [
#             x
#             for x in os.listdir(tasklists_folder)
#             if os.path.isfile(os.path.join(tasklists_folder, x))
#         ]
#         if tasklists:
#             for tl in tasklists:
#                 click.echo("    - {}".format(tl))
#             click.echo()
#
#
# # @last.command("debug")
# # @click.pass_context
# # def debug_last(ctx):
# #     """Re-runs the last freckle run directly using ansible-playbook and verbose output."""
# #
# #     context = ctx.obj["context"]
# #     cnf = context.cnf
# #     last_run_folder = cnf.config_dict.get(
# #         "current_run_folder", FRECKLES_CURRENT_RUN_SYMLINK
# #     )
# #
# #     last_run_debug_folder = os.path.join(last_run_folder, "debug")
# #     last_run_debug_script = os.path.join(last_run_debug_folder, "debug_all_plays.sh")
# #
# #     run_env = os.environ.copy()
# #
# #     # proc = subprocess.Popen(last_run_debug_script, stdout=subprocess.PIPE, stderr=sys.stdout.fileno(),
# #     proc = subprocess.Popen(
# #         last_run_debug_script, stdin=subprocess.PIPE, shell=True, env=run_env
# #     )
# #
# #     proc.communicate()
# #     # for line in iter(proc.stdout.readline, ''):
# #     # click.echo(line, nl=False)
#
#
# @runs.command("log")
# @click.option("--follow", "-f", help="follow the log file", is_flag=True, default=False)
# @click.option(
#     "--nsbl",
#     "-n",
#     help="use thensbl log file instead of the (more detailed) Ansible one",
#     is_flag=True,
#     default=False,
# )
# @click.pass_context
# def log_current(ctx, follow, nsbl):
#     """Prints out the last runs ansible log (verbose).
#
#     The normal output of any 'freckles' command is short-form. Which helps see what's going on. This is not helpful when there is an issue or during development of roles, adapters, blueprints or frecklecutables.
#
#     Instead of manually tailing that particular log-file, this commands lets you do that a tad quicker.
#     """
#
#     context = ctx.obj["context"]
#
#     cnf = context.cnf.get_interpreter("adapter_run_config_nsbl")
#
#     last_run_folder = cnf.config.get("add_symlink_to_env")
#     last_run_log_folder = os.path.join(last_run_folder, "logs")
#
#     if nsbl:
#         ansible_log_file = os.path.join(last_run_log_folder, "nsbl_run_log")
#     else:
#         ansible_log_file = os.path.join(last_run_log_folder, "ansible_run_log")
#
#     if not follow:
#         f = subprocess.Popen(["cat", ansible_log_file], shell=False)
#
#     else:
#
#         link_target = os.readlink(last_run_folder)
#
#         f = None
#
#         while True:
#
#             if not os.path.exists(ansible_log_file):
#                 time.sleep(1)
#                 continue
#
#             if not f:
#                 f = subprocess.Popen(["tail", "-F", ansible_log_file], shell=False)
#
#             time.sleep(1)
#             new_link_target = os.readlink(last_run_folder)
#             if new_link_target != link_target:
#                 f.terminate()
#                 f = None
#                 link_target = new_link_target
