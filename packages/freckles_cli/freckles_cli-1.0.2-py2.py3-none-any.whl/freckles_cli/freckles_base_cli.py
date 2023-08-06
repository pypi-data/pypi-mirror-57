# -*- coding: utf-8 -*-

import abc
import logging
import os
import sys

import click
import click_completion
import click_log
import six
from click import Choice
from colorama import init as colorama_init
from omegaconf import OmegaConf
from plumbum import local

from freckles import print_version
from freckles.context.run_config import FrecklesRunConfig
from freckles.defaults import FRECKLES_CONFIG_DIR, DEFAULT_FRECKLES_SSH_SESSION_SOCK
from freckles.exceptions import InvalidFreckletException, FreckletException
from freckles.freckles import Freckles
from freckles.frecklet.vars import VarsInventory
from frkl import VarsType
from frutils import readable_yaml, special_dict_to_dict
from frutils.exceptions import FrklException
from frutils.frutils_cli import output_to_terminal
from frutils.utils.ssh import get_agent_ssh_keys, add_default_ssh_key_to_agent
from ting.exceptions import TingException

log = logging.getLogger("freckles")
click_log.basic_config(log)

# optional shell completion
click_completion.init()
colorama_init()


def create_context(ctx, force=False):

    try:

        if ctx.obj is None:
            ctx.obj = {}

        config = ctx.obj.get("config", None)
        repos = ctx.obj.get("repos", None)
        use_community = ctx.obj.get("use_community", None)
        result_callbacks = ctx.obj.get("result", None)
        callbacks = ctx.obj.get("callback", None)

        if (config is None or repos is None or use_community is None) and not force:
            return False

        if config is None:
            config = []
            ctx.obj["config"] = config
        if repos is None:
            repos = []
            ctx.obj["repos"] = repos
        if use_community is None:
            use_community = False

        log.debug("Creating context...")
        log.debug("  config: {}".format(config))
        log.debug("  repos: {}".format(repos))
        log.debug("  use_community: {}".format(use_community))

        config = list(config)
        if use_community:
            config.insert(0, "community")

        if result_callbacks:
            config.append({"result": result_callbacks})
        if callbacks:
            config.append({"callback": callbacks})

        freckles = Freckles(
            context_config=config, extra_repos=repos, config_repos=FRECKLES_CONFIG_DIR
        )
        ctx.obj["freckles"] = freckles
        ctx.obj["context"] = freckles.get_context("default")

        return freckles
    except (Exception) as e:
        handle_exception(e)
        log.debug(e, exc_info=1)
        click.echo("Can't create context: {}".format(e))
        sys.exit(1)


def handle_exception(exc, exit=True, exit_code=1, frecklet=None, frecklet_name=None):

    log.debug(exc, exc_info=1)
    # click.echo("Can't create context: {}".format(e))

    if isinstance(exc, TingException):

        root_exc = exc.root_exc
        if isinstance(root_exc, FreckletException):
            exc = root_exc
        else:
            exc = FreckletException(
                frecklet=frecklet, parent_exception=exc, frecklet_name=frecklet_name
            )
    if not isinstance(exc, FrklException):
        exc = FrklException(exc)

    if hasattr(exc, "reason"):
        reason = exc.reason

        if (
            reason is not None
            and "Invalid frecklet: content needs to be a list or dict" in reason
        ):
            exc = InvalidFreckletException(
                frecklet=frecklet, frecklet_name=frecklet_name, parent_exception=exc
            )

    click.echo()
    exc.print_message()

    if exit:
        sys.exit(exit_code)


def set_config(ctx, param, value):

    if ctx.obj is None:
        ctx.obj = {}
    ctx.obj["config"] = value
    create_context(ctx)


def set_result(ctx, param, value):

    if ctx.obj is None:
        ctx.obj = {}
    ctx.obj.setdefault("result", []).extend(value)
    create_context(ctx)


def set_callback(ctx, param, value):

    if ctx.obj is None:
        ctx.obj = {}
    ctx.obj.setdefault("callback", []).extend(value)
    create_context(ctx)


def set_vars(ctx, param, value):

    if ctx.obj is None:
        ctx.obj = {}
    ctx.obj["vars"] = value


def set_repos(ctx, param, value):
    if ctx.obj is None:
        ctx.obj = {}
    ctx.obj["repos"] = value
    try:
        create_context(ctx)
    except (Exception) as e:
        log.debug(e, exc_info=1)
        click.echo("Problems adding repos'{}': {}".format(value, e))
        sys.exit()


def use_community_repo(ctx, param, value):
    if ctx.obj is None:
        ctx.obj = {}
    if value is None:
        value = False
    ctx.obj["use_community"] = value
    try:
        create_context(ctx)
    except (Exception) as e:
        click.echo(e)
        sys.exit()


def check_askpass_available(ctx, param, value):

    if value:
        try:
            local["sshpass"]
            return True
        except (Exception) as e:
            log.debug("failed to load 'sshpass': {}".format(e))

            click.echo(
                "\nYou specified the '--ask-pass' flag, but the 'sshpass' package is not available on this system.\n\nYou can either install it manually, for details and security implications, check:\n\nhttps://www.cyberciti.biz/faq/noninteractive-shell-script-ssh-password-provider/\n\nOr use the 'pkg-askpass-installed' frecklecutable:\n\nfrecklecute sshpass-installed\n"
            )

            sys.exit(1)


def run_frecklet(
    ctx, frecklet, freckles_context, run_config, vars, dump_frecklet=False
):

    frecklet_name = frecklet.frecklet_name
    ctx.obj["frecklet_name"] = frecklet_name

    if dump_frecklet:

        dumped = {}
        dumped_frecklet = {}
        dumped_frecklet[frecklet.id] = vars
        dumped["frecklets"] = [dumped_frecklet]

        yaml_string = readable_yaml(dumped, ignore_aliases=True)
        # click.echo()
        output_to_terminal(yaml_string)
        sys.exit()

    fx = frecklet.create_frecklecutable(context=freckles_context)

    elevated = ctx.params.get("elevated", None)
    if elevated == "elevated":
        elevated = True
    elif elevated == "not_elevated":
        elevated = False
    else:
        elevated = None

    if (
        run_config.host not in ["localhost", "127.0.0.1"]
        and run_config.login_pass is None
    ):

        try:
            ssh_agent_keys = None
            ssh_agent_keys = get_agent_ssh_keys(sock=DEFAULT_FRECKLES_SSH_SESSION_SOCK)

            if ssh_agent_keys:
                os.environ["SSH_AUTH_SOCK"] = DEFAULT_FRECKLES_SSH_SESSION_SOCK
            else:
                ssh_agent_keys = get_agent_ssh_keys()

        except (Exception):
            pass

        if not ssh_agent_keys:

            keep_ssh_agent = freckles_context.config_value("keep_ssh_agent")

            def callback():
                click.echo(
                    "ssh-key is password protected, and no running ssh-agent found."
                )
                if keep_ssh_agent:
                    click.echo(
                        " -> 'keep_ssh_agent' config option set, will start ssh-agent and keep it running after this execution finishes..."
                    )
                else:
                    click.echo(
                        " -> starting temporary ssh-agent which will be stopped after this run finishes..."
                    )
                click.echo()
                pw = click.prompt("Please enter ssh-key password", hide_input=True)
                click.echo()
                return pw

            try:
                log.debug("No ssh keys in ssh-agent (or ssh-agent not running).")
                add_default_ssh_key_to_agent(
                    ssh_agent_sock_path=DEFAULT_FRECKLES_SSH_SESSION_SOCK,
                    kill_agent_at_exit=not keep_ssh_agent,
                    password_callback=callback,
                )
            except (Exception) as e:
                log.debug("Can't auto-load ssh key, trying without...")
                log.debug(e, exc_info=1)
                # handle_exception(e)

                # successfully_added basically only checks whether the user pressed Ctrl-C

        else:
            log.debug(
                "At least one ssh key in ssh-agent, assuming this will be enough: {}".format(
                    ssh_agent_keys
                )
            )
    try:

        inventory = VarsInventory(vars)
        result = fx.run_frecklecutable(
            inventory=inventory, run_config=run_config, run_vars={}, elevated=elevated
        )
    except (Exception) as e:
        handle_exception(e, frecklet=fx, frecklet_name=frecklet_name)

    if not run_config.no_run:

        if result:
            # result_dict = result.result
            success = result.success
        else:
            success = False

        if success:
            exit_code = 0
        else:
            exit_code = 11

        sys.exit(exit_code)

    click.echo("\n'no-run' specified, not running generated frecklecutable...\n")
    click.echo("\nRun configuration:\n")
    click.echo(readable_yaml(run_config.config, indent=4))
    click.echo("\nVariables:\n")
    click.echo(readable_yaml(inventory.get_vars(hide_secret=False), indent=4))

    # TODO: also display previous runs

    click.echo("Run {}".format(result.run_id))
    click.echo("Generated environment: {}".format(result.run_env["env_dir"]))
    click.echo("\nTasks:\n")
    click.echo(readable_yaml(result.task_list))

    click.echo()


def get_common_options(print_version_callback=print_version):

    version_option = click.Option(
        param_decls=["--version"],
        help="the version of freckles you are using",
        type=bool,
        is_flag=True,
        is_eager=True,
        expose_value=False,
        callback=print_version_callback,
    )
    # output_option = click.Option(
    #     param_decls=["--output", "-o"], help="the output format to use"
    # )
    vars_option = click.Option(
        param_decls=["--vars", "-v"],
        help="additional vars, higher priority than frecklet vars, lower priority than potential user input",
        multiple=True,
        type=VarsType(),
        callback=set_vars,
        is_eager=True,
        expose_value=True,
    )
    community_option = click.Option(
        param_decls=["--community"],
        help="use resources from the freckles community repo",
        multiple=False,
        callback=use_community_repo,
        is_eager=True,
        expose_value=True,
        is_flag=True,
    )
    repo_option = click.Option(
        param_decls=["--repo", "-r"],
        help="additional repo(s) to use",
        multiple=True,
        callback=set_repos,
        is_eager=True,
        expose_value=True,
        default=[],
        metavar="REPO",
    )
    config_option = click.Option(
        param_decls=["--context", "-c"],
        help="select context/config profile(s)",
        multiple=True,
        type=str,
        callback=set_config,
        default=[],
        is_eager=True,
        expose_value=True,
        metavar="CONTEXT_ITEM",
    )
    callback_option = click.Option(
        param_decls=["--callback"],
        help="whether and how to output the run log",
        multiple=True,
        callback=set_callback,
        required=False,
        metavar="CALLBACK_NAME",
    )
    result_option = click.Option(
        param_decls=["--result"],
        help="whether and how to output a potential result",
        multiple=True,
        callback=set_result,
        type=Choice(["pretty", "json", "false"]),
        required=False,
        default=["pretty"],
        metavar="RESULT_CALLBACK",
    )
    target_option = click.Option(
        param_decls=["--target", "-t"],
        help="the (default) target to use",
        multiple=False,
        type=str,
        default="localhost",
    )
    ask_sudo_option = click.Option(
        param_decls=["--ask-become-pass"],
        help="ask for the become/sudo password",
        multiple=False,
        type=bool,
        default=False,
        is_flag=True,
        is_eager=True,
        callback=check_askpass_available,
        expose_value=True,
    )
    ask_pass_option = click.Option(
        param_decls=["--ask-login-pass"],
        help="ask for the connection password of the user",
        multiple=False,
        type=bool,
        default=False,
        is_flag=True,
        is_eager=True,
        callback=check_askpass_available,
        expose_value=True,
    )
    elevated_option = click.Option(
        param_decls=["--elevated", "-e", "elevated"],
        help="indicate that this run needs elevated permissions",
        flag_value="elevated",
        required=False,
    )
    not_elevated_option = click.Option(
        param_decls=["--not-elevated", "-ne", "elevated"],
        help="indicate that this run doesn't need elevated permissions",
        flag_value="not_elevated",
        required=False,
    )
    no_run_option = click.Option(
        param_decls=["--no-run"],
        help="create the run environment (if applicable), but don't run the frecklet",
        flag_value=True,
        default=None,
    )

    result = [
        community_option,
        repo_option,
        config_option,
        callback_option,
        result_option,
        no_run_option,
        ask_sudo_option,
        ask_pass_option,
        elevated_option,
        not_elevated_option,
        vars_option,
        target_option,
        version_option,
    ]
    return result


@six.add_metaclass(abc.ABCMeta)
class FrecklesBaseCommand(click.MultiCommand):
    """Base class to provide a command-based (similar to e.g. git) cli for frecklecute.
    """

    def __init__(
        self,
        print_version_callback=print_version,
        name=None,
        invoke_without_command=False,
        no_args_is_help=None,
        chain=False,
        result_callback=None,
        **kwargs
    ):

        super(FrecklesBaseCommand, self).__init__(
            name=None,
            invoke_without_command=invoke_without_command,
            no_args_is_help=False,
            chain=False,
            result_callback=None,
            **kwargs
        )

        self.print_version_callback = print_version_callback
        self.params[:0] = get_common_options(
            print_version_callback=self.print_version_callback
        )

        self.context = None
        self.config = None
        self.vars = None
        self.repos = None
        self.no_run = None
        self.dump_frecklet = None
        self.target_string = None
        self.target_dict = None
        self.output_format = None
        self.elevated = None

        self.extra_vars = None

        self.run_config = None
        self._init_done = False

    def init_parent_command(self, ctx):

        if self.run_config is not None:
            return

        self.no_run = ctx.params.get("no_run", False)
        self.dump_frecklet = ctx.params.get("dump", False)
        target_string = ctx.params.get("target", "localhost")
        self.output_format = ctx.params.get("output", None)
        self.elevated = ctx.params.get("elevated", None)
        self.callback_name = "freckles_callback"

        if ctx.obj is None or "context" not in ctx.obj.keys():
            create_context(ctx, force=True)

        self.context = ctx.obj["context"]
        self.config = ctx.obj["config"]
        self.repos = ctx.obj["repos"]

        self.target_string = target_string
        self.target_dict = {}
        ask_login_pass = ctx.params.get("ask_login_pass", False)
        if ask_login_pass:
            self.target_dict["login_pass"] = "::ask::"
        else:
            self.target_dict["login_pass"] = None
        ask_become_pass = ctx.params.get("ask_become_pass", False)
        if ask_become_pass:
            self.target_dict["become_pass"] = "::ask::"
        else:
            self.target_dict["become_pass"] = None

        # self.extra_vars = merge_list_of_dicts(ctx.obj.get("vars", []))
        v = ctx.obj.get("vars", [])
        if v:
            self.extra_vars = special_dict_to_dict(OmegaConf.merge(*v))
        else:
            self.extra_vars = {}
        self._init_done = True

        # self.control_dict = self.get_control_dict()
        self.run_config = self.get_run_config()

    def get_run_config(self):

        if not self._init_done:
            raise Exception(
                "Initializion for frecklet_base_cli not done yet, can't continue"
            )

        if self.elevated == "elevated":
            elevated = True
        else:
            elevated = False

        run_config = FrecklesRunConfig(
            target_dict=self.target_dict,
            target_string=self.target_string,
            elevated=elevated,
            no_run=self.no_run,
        )

        # dict_merge(run_config, run_target.config, copy_dct=False)
        # if self.output_format is not None:
        #     run_config["output"] = self.output_format
        # run_config["no_run"] = self.no_run
        # run_config["dump_frecklet"] = self.dump_frecklet
        # run_config["callback"] = "freckles_callback"

        return run_config

    @abc.abstractmethod
    def list_freckles_commands(self, ctx):

        pass

    @abc.abstractmethod
    def get_freckles_command(self, ctx, command_name):

        pass

    def list_commands(self, ctx):
        if ctx.obj.get("help_only", False):
            return []

        self.init_parent_command(ctx)
        return self.list_freckles_commands(ctx)

    def get_command(self, ctx, name):
        try:
            self.init_parent_command(ctx)

            return self.get_freckles_command(ctx, name)
        except (Exception) as e:
            log.debug(e, exc_info=1)
            click.echo()
            click.echo(e)
            sys.exit(2)
