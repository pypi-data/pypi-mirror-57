# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import getpass
import logging
import os
import sys

import click
import psutil
from ruamel.yaml import YAML

from freckles.defaults import DEFAULT_FRECKLES_SSH_SESSION_SOCK
from freckles_cli.freckles_base_cli import handle_exception
from frutils.utils.ssh import (
    get_agent_ssh_keys,
    agent_is_available,
    add_default_ssh_key_to_agent,
)

yaml = YAML(typ="safe")

log = logging.getLogger("freckles")


@click.group()
@click.pass_context
def ssh(ctx):
    """
    'ssh'-related sub-commands.
    """

    pass


@ssh.command("info")
@click.pass_context
def info(ctx):

    aa = agent_is_available()

    click.echo()
    click.echo("ssh agent available: {}".format(aa))
    keys = get_agent_ssh_keys()
    click.echo("(unlocked) ssh keys: ", nl=False)
    if not keys:
        click.echo("-")
    else:
        click.echo()
        for k in keys:
            click.echo("  - {}".format(k))

    click.echo()

    aa = agent_is_available(sock=DEFAULT_FRECKLES_SSH_SESSION_SOCK)

    click.echo()
    click.echo("freckles ssh agent available: {}".format(aa))
    keys = get_agent_ssh_keys(sock=DEFAULT_FRECKLES_SSH_SESSION_SOCK)
    click.echo("(unlocked) ssh keys: ", nl=False)
    if not keys:
        click.echo("-")
    else:
        click.echo()
        for k in keys:
            click.echo("  - {}".format(k))

    click.echo()


@ssh.command("kill-agent")
def kill_agent():

    # if not os.path.exists(DEFAULT_FRECKLES_SSH_SESSION_SOCK):
    #     click.echo()
    #     click.echo("freckles ssh socket does not exists, not doing anything...")

    username = getpass.getuser()
    click.echo()
    for process in psutil.process_iter():
        try:
            pinfo = process.as_dict(attrs=["pid", "name", "username", "cmdline"])
            # pinfo = process.as_dict()
        except psutil.NoSuchProcess:
            pass
        if pinfo["username"] != username:
            continue

        if pinfo["name"] != "ssh-agent":
            continue

        killed = False
        for token in pinfo["cmdline"]:
            if DEFAULT_FRECKLES_SSH_SESSION_SOCK in token:
                click.echo("Killing process: {}".format(pinfo["pid"]))
                process.kill()
                os.unlink(DEFAULT_FRECKLES_SSH_SESSION_SOCK)
                killed = True

        if not killed:
            click.echo("No running freckles ssh-agent found.")

        click.echo()


@ssh.command("start-agent")
def start_agent():

    ssh_agent_keys = None
    try:
        ssh_agent_keys = get_agent_ssh_keys()
    except (Exception):
        pass

    if ssh_agent_keys:
        click.echo()
        click.echo(
            "ssh agent running and at least one ssh key available, doing nothing..."
        )
        sys.exit()

    try:
        ssh_agent_keys = get_agent_ssh_keys(sock=DEFAULT_FRECKLES_SSH_SESSION_SOCK)
    except (Exception):
        pass

    if not ssh_agent_keys:

        try:

            def callback():
                pw = click.prompt("Please enter ssh-key password", hide_input=True)
                return pw

            add_default_ssh_key_to_agent(
                ssh_agent_sock_path=DEFAULT_FRECKLES_SSH_SESSION_SOCK,
                kill_agent_at_exit=False,
                password_callback=callback,
            )

        except (Exception) as exc:
            handle_exception(exc)
