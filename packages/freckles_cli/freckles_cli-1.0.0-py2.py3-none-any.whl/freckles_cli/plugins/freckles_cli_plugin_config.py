# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import io
import os
import sys

import click
from click import Choice

from freckles.context.config import is_unlocked, unlock
from freckles.defaults import EXTERNAL_FOLDER as FRECKLES_EXTERNAL_FOLDER


@click.group()
@click.pass_context
def config(ctx):
    """'config'-related tasks.

    Currently, the only available command is 'unblock' to unblock certain security-related features of freckles.
    """

    pass


@config.command(name="unlock")
def unlock_config():
    """Unlock configuration for advanced usage.

    By default, freckles does not allow the use of remote repositories (except for the 'community' one), as well as other
    security-relevant features. Those must be explicitly enabled after unlocking the configuration, which is done with this
    command.

    You can do this manually by creating a file '$HOME/.config/freckles/.freckles_config_unlock' with this content (one line):


    I know what I'm doing and this is not just copy and pasted from a random blog post on the internet. Also, I accept the freckles license.


    For more information, please check out: https://freckles.io/doc/configuration

    """

    unlocked = is_unlocked()

    if unlocked:
        click.echo()
        click.echo("freckles configuration already unlocked, doing nohting...")
        click.echo()
        sys.exit()

    unlock_text_file = os.path.join(
        FRECKLES_EXTERNAL_FOLDER, "docs", "unlock_config_text.md"
    )

    with io.open(unlock_text_file, "r", encoding="utf-8") as f:
        unlock_text = f.read()

    # rendered = mdv.main(unlock_text, no_colors=True, header_nrs="1-")
    click.echo()
    click.echo(unlock_text)

    click.echo()

    input = click.prompt(
        "Unlock config, accept license",
        default="no",
        type=Choice(choices=["yes", "no"], case_sensitive=False),
    )

    if input.lower() == "no":
        click.echo("\nNo changes made.")
        sys.exit(0)

    unlock()
