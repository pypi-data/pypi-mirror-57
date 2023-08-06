# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import logging
import os
import platform
import shutil
import stat
import sys

import click
import requests
from cursor import cursor

from freckles.context.config import is_unlocked
from freckles.defaults import (
    FRECKLES_CONFIG_DIR,
    FRECKLES_SHARE_DIR,
    FRECKLES_CACHE_BASE,
    FRECKLES_RUN_ARCHIVE,
)
from freckles.utils.versions import get_versions
from freckles_cli.freckles_base_cli import handle_exception
from frutils.frutils_cli import CursorOff

log = logging.getLogger("freckles")

DOWNLOAD_URLS = {
    "stable": {
        "Linux": "https://dl.frkl.io/linux-gnu/freckles",
        "Darwin": "https://dl.frkl.io/darwin/freckles",
    },
    "dev": {
        "Linux": "https://s3-eu-west-1.amazonaws.com/dev.dl.frkl.io/linux-gnu/freckles",
        "Darwin": "https://s3-eu-west-1.amazonaws.com/dev.dl.frkl.io/darwin/freckles",
    },
}


@click.group(name="env")
@click.pass_context
def self_command(ctx):
    """Manage/display details about this freckles install."""
    pass


@self_command.command(name="clean")
@click.option(
    "--all",
    "-a",
    help="delete all freckles-related data from this machine",
    is_flag=True,
)
@click.option("--cache", "-c", help="delete freckles cache directory", is_flag=True)
@click.option("--share", "-c", help="delete freckles share directory", is_flag=True)
@click.option(
    "--runs", "-r", help="delete freckles runs archive directory", is_flag=True
)
@click.pass_context
def clean(ctx, all, cache, share, runs):
    """Clean up the certain aspects of this freckles install."""

    with CursorOff():
        click.echo()
        if all:
            cache = True
            share = True
            runs = True

        if not cache and not share and not runs:
            click.echo("No items to clean up specified, doing nothing...")
            sys.exit()

        if cache:
            click.echo(
                "- deleting freckles cache dir '{}'".format(FRECKLES_CACHE_BASE),
                nl=False,
            )
            if os.path.exists(FRECKLES_CACHE_BASE):
                shutil.rmtree(FRECKLES_CACHE_BASE)
            click.echo(": done")

        if runs:
            click.echo(
                "- deleting freckles runs archive '{}'".format(FRECKLES_RUN_ARCHIVE),
                nl=False,
            )
            if os.path.exists(FRECKLES_RUN_ARCHIVE):
                shutil.rmtree(FRECKLES_RUN_ARCHIVE)
            click.echo(": done")

        if share:
            click.echo(
                "- deleting freckles share dir '{}'".format(FRECKLES_SHARE_DIR),
                nl=False,
            )
            if os.path.exists(FRECKLES_SHARE_DIR):
                shutil.rmtree(FRECKLES_SHARE_DIR)
            click.echo(": done")


@self_command.command(name="info")
@click.pass_context
def info(ctx):
    """Print information about the current freckles install.
    """

    is_pyinstaller_bundle = (
        hasattr(sys, "frozen") and getattr(sys, "frozen") and hasattr(sys, "_MEIPASS")
    )
    if is_pyinstaller_bundle:
        exe = sys.executable
        exe_type = "binary"
    else:
        exe = sys.argv[0]
        exe_type = "python environment"

    click.echo()
    click.echo("executable: {}".format(os.path.realpath(exe)))
    click.echo("executable type: {}".format(exe_type))
    click.echo("config dir: {}".format(FRECKLES_CONFIG_DIR))
    click.echo("config unlocked: {}".format("yes" if is_unlocked() else "no"))
    click.echo("share dir: {}".format(FRECKLES_SHARE_DIR))
    click.echo("runs archive: {}".format(FRECKLES_RUN_ARCHIVE))
    click.echo("cache dir: {}".format(FRECKLES_CACHE_BASE))
    click.echo("freckles version: {}".format(get_versions()["freckles"]))


@self_command.command()
@click.option(
    "--all",
    "-a",
    help="display version information for all (frkl-) project dependencies",
    is_flag=True,
)
@click.pass_context
def version(ctx, all):
    """
    Display freckles version information.
    """

    click.echo()
    versions = get_versions()

    if all:
        for k, v in versions.items():
            print("{}: {}".format(k, v))
        sys.exit()

    from freckles import __version__

    print(__version__)


@self_command.command(name="update")
@click.option(
    "--dev", help="download latest development version instead of stable", is_flag=True
)
def update(dev):
    """
    Update the freckles binary.
    """

    is_pyinstaller_bundle = (
        hasattr(sys, "frozen") and getattr(sys, "frozen") and hasattr(sys, "_MEIPASS")
    )
    # is_pyinstaller_bundle = True

    if not is_pyinstaller_bundle:
        click.echo()
        click.echo("This is not a 'freckles' binary bundle, updated not supported.")
        click.echo()
        sys.exit(1)

    # path = os.path.realpath(sys.argv[0])
    path = os.path.realpath(sys.executable)
    # print("exe: {}".format(path))
    # path = os.path.realpath("/home/markus/.local/share/freckles/bin/frecklecute")

    if not path.endswith(os.path.sep + "freckles"):
        click.echo()
        click.echo(
            "Can't update, not a supported binary name (must be 'freckles'): {}".format(
                os.path.basename(path)
            )
        )
        click.echo()
        sys.exit()

    if not dev:
        version = "stable"
    else:
        version = "dev"

    pf = platform.system()
    url = DOWNLOAD_URLS[version].get(pf, None)
    if url is None:
        click.echo()
        click.echo("Can't update, platform '{}' not supported.".format(pf))
        click.echo()
        sys.exit(1)

    click.echo()
    click.echo("downloading: {}".format(url))

    temp_path = path + ".tmp"
    with open(temp_path, "wb") as f:

        try:
            cursor.hide()
            r = requests.get(url, allow_redirects=True)
            f.write(r.content)
        except (Exception) as e:
            click.echo("   -> download error: {}".format(e))
            click.echo()
            sys.exit(1)
        finally:
            cursor.show()

    orig_path = path + ".orig"
    try:
        st = os.stat(temp_path)
        os.chmod(temp_path, st.st_mode | stat.S_IEXEC)
        click.echo("updating freckles binary: {}".format(path))
        os.rename(path, orig_path)
        os.rename(temp_path, path)
    except Exception() as e:
        handle_exception(e)
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        if not os.path.exists(path) and os.path.exists(orig_path):
            os.rename(orig_path, path)
        if os.path.exists(orig_path):
            os.unlink(orig_path)

    click.echo()
