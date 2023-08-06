# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import copy
import io
import logging
import os
import signal
import subprocess
import sys
import time
from secrets import token_urlsafe

import cursor
from future import standard_library

try:
    from shutil import which
except Exception:
    # python2
    from distutils.spawn import find_executable as which
from plumbum import local

from frutils import readable_yaml
from .nsbl_callback import NsblPrintCallbackAdapter

standard_library.install_aliases()


log = logging.getLogger("nsbl")

DEFAULT_PEXPECT_TIMEOUT = 36000


class NsblRunner(object):
    def __init__(self, nsbl):
        """Class to kick off rendering and running the ansible environment in question.

        Args:
          nsbl (Nsbl): the Nsbl object holding the (processed) configuration
        """
        self.nsbl = nsbl

    def process_secret_vars_env(
        self,
        run_folder,
        run_env,
        sudo_password,
        ssh_password,
        secret_vars,
        elevated_permissions_required,
        passwordless_sudo_possible,
    ):

        # adding secure_vars
        for sec_var_alias, sec_var_details in secret_vars.items():
            if sec_var_details["type"] == "environment":
                run_env[sec_var_alias] = sec_var_details["value"]
            else:
                raise Exception(
                    "Secure var type '{}' not supported.".format(
                        sec_var_details["type"]
                    )
                )

        if sudo_password is not None:
            if elevated_permissions_required:
                if passwordless_sudo_possible:
                    ask_sudo = False
                else:
                    ask_sudo = True
            else:
                ask_sudo = False
        else:
            ask_sudo = False

        if ask_sudo:
            run_env["NSBL_SUDO_PASSWORD"] = sudo_password
        if ssh_password is not None:
            run_env["NSBL_SSH_PASSWORD"] = ssh_password

    def process_secret_vars_vault(
        self,
        run_folder,
        run_env,
        encryption_key,
        sudo_password,
        ssh_password,
        secret_vars,
        elevated_permissions_required,
        passwordless_sudo_possible,
    ):

        vars_dict = copy.copy(secret_vars)
        if sudo_password is not None:
            if elevated_permissions_required:
                if passwordless_sudo_possible:
                    ask_sudo = False
                else:
                    ask_sudo = True
            else:
                ask_sudo = False
        else:
            ask_sudo = False

        if ask_sudo:
            vars_dict["ansible_become_pass"] = sudo_password
        if ssh_password is not None:
            vars_dict["ansible_ssh_pass"] = ssh_password

        # create_vault_script_path = os.path.join(
        #     os.path.dirname(__file__), "external", "scripts", "create-vault.sh"
        # )
        create_vault_script_path = os.path.join(run_folder, "create-vault.sh")
        create_vault_script = local[create_vault_script_path]

        play_folder = os.path.join(run_folder, "plays")

        process = None
        vault_pipe = os.path.join(play_folder, "unencrypted_vault")
        pw_file_pipe = os.path.join(play_folder, "vault_pw")
        try:
            # os.mkfifo(pw_file_pipe, mode=0o700)
            # os.mkfifo(vault_pipe, mode=0o700)
            with io.open(pw_file_pipe, "w+") as fh:
                fh.write("")
            os.chmod(pw_file_pipe, 0o600)
            with io.open(vault_pipe, "w+") as fh:
                fh.write("")
            os.chmod(vault_pipe, 0o600)

            with io.open(pw_file_pipe, "w", encoding="UTF-8") as f:
                f.write("{}\n".format(encryption_key))

            with io.open(vault_pipe, "w", encoding="UTF-8") as f:
                f.write("{}\n".format(readable_yaml(vars_dict, ignore_aliases=True)))

            # rc, stdout, stderr = create_vault_script(play_folder)
            process = create_vault_script.popen([play_folder], env=run_env)
            process.wait()

            rc = process.returncode

            if rc != 0:
                raise Exception("Return code of 'create-vault.sh' script not 0")
        except (Exception) as e:
            vault_file = os.path.join(play_folder, "run_vault.yml")
            if os.path.exists(vault_file):
                os.unlink(vault_file)

            raise Exception("Could not create vault: {}".format(e))
        finally:
            if os.path.exists(pw_file_pipe):
                os.unlink(pw_file_pipe)
            if os.path.exists(vault_pipe):
                os.unlink(vault_pipe)

    def run(
        self,
        run_folder=None,
        global_vars=None,
        force=False,
        ansible_args="",
        elevated_permissions_required=None,
        passwordless_sudo_possible=None,
        sudo_password=None,
        ssh_password=None,
        extra_env_vars=None,
        secure_vars=None,
        callback=None,
        callback_adapter=None,
        add_timestamp_to_env=False,
        add_symlink_to_env=False,
        no_run=False,
        pre_run_callback=None,
        extra_paths=None,
        show_tasks_with_password_in_log=False,
        use_mitogen=False,
        use_ara=False,
        parent_task=None,
        **kwargs
    ):
        """Starts the ansible run, executing all generated playbooks.

        By default the 'nsbl_internal' ansible callback is used, which outputs easier to read outputs/results. You can, however,
        also use the callbacks that come with ansible, like 'default', 'skippy', etc.

        Args:
          run_folder (str): the target directory where the ansible environment should be rendered
          global_vars (dict): vars to be rendered on top of each playbook
          force (bool): whether to overwrite potentially existing files at the target (most likely an old rendered ansible environment)
          ansible_args (str): verbosity arguments to ansible-playbook command
          elevated_permissions_required (bool): whether to include the '--ask-become-pass' arg to the ansible-playbook call
          passwordless_sudo_possible (bool): whether passwordless sudo is possible on the host(s)
          sudo_password (str): if provided, it will be used instead of asking for a password
          ssh_password (str): if provided, it will be used instead of asking for a password
          extra_env_vars (dict): a dict with vars to put into the run environment
          secure_vars (dict): other vars to keep secure
          callback (str): the callback to use for the ansible run. default is 'default'
          callback_adapter: the callback adapter to use
          add_timestamp_to_env (bool): whether to append a timestamp to the run directory (default: False)
          add_symlink_to_env (str): whether to add a symlink to the run directory (will be deleted if exists already and force is specified) - default: False, otherwise path to symlink
          no_run (bool): whether to only render the environment, but not run it
          pre_run_callback (function): a callback to execute after the environment is rendered, but before the run is kicked off
          extra_paths (str): a list of extra paths that should be exported for the nsbl run
          show_tasks_with_password_in_log (bool): whether to show tasks that contain a password variable in the log (only enable for debugging!)
          use_mitogen (bool): whether to use mitogen to speed up playbook run
          use_ara (bool): use ara (https://ara.readthedocs.io)
          parent_task (TaskDetail): task object to update
        Return:
          dict: the parameters of the run
        """

        env_dir = None

        if run_folder is None:
            run_folder = os.path.join(os.getcwd(), "nsbl_env")

        if callback is None:
            callback = "default"

        if callback_adapter is None:
            callback_adapter = NsblPrintCallbackAdapter()

        # debug_callback = False
        # if debug_callback:
        #     callback_adapter = NsblPrintCallbackAdapter()
        #     callback = "freckles_callback"
        # else:
        #     if isinstance(callback, string_types):
        #         callback_adapter = NsblPrintCallbackAdapter()
        #     else:
        #         callback_adapter = FrecklesCallbackAdapter(self.nsbl, callback)
        #         callback = "freckles_callback"

        # try:
        #     term = Terminal()
        # except (Exception):
        #     # no terminal then, fine...
        #     # probably because the TERM env var is not set
        #     term = None

        try:
            parameters = None
            proc = None
            parameters = self.nsbl.render(
                run_folder,
                global_vars=global_vars,
                extract_vars=True,
                force=force,
                elevated_permissions_required=elevated_permissions_required,
                passwordless_sudo_possible=passwordless_sudo_possible,
                secure_vars=secure_vars,
                ansible_args=ansible_args,
                callback=callback,
                add_timestamp_to_env=add_timestamp_to_env,
                add_symlink_to_env=add_symlink_to_env,
                extra_paths=":".join(extra_paths),
                show_tasks_with_password_in_log=show_tasks_with_password_in_log,
                use_mitogen=use_mitogen,
                use_ara=use_ara,
                parent_task=parent_task,
            )
            callback_adapter.set_environment_parameters(parameters)

            env_dir = parameters["env_dir"]
            if pre_run_callback:
                pre_run_callback(env_dir)

            if no_run:
                log.debug("Not running environment due to 'no_run' flag set.")
                return parameters

            run_env = os.environ.copy()
            if callback.startswith("nsbl_internal"):
                run_env["NSBL_ENVIRONMENT"] = "true"

            # try to set 'USER' environment var, as that is sometimes not set in a docker environment
            if "USER" not in run_env.keys():
                whoami = which("whoami")

                if whoami:
                    which_cmd = local[whoami]
                    rc, stdout, stderr = which_cmd.run()

                    if rc == 0:
                        run_env["USER"] = stdout

            def preexec_function():
                # Ignore the SIGINT signal by setting the handler to the standard
                # signal handler SIG_IGN.
                signal.signal(signal.SIGINT, signal.SIG_IGN)

            script = parameters["run_playbooks_script"]

            path = os.getenv("PATH")
            path = "{}:{}".format(":".join(extra_paths), path)
            log.debug("PATHS for Ansible run: {}".format(path))

            if extra_env_vars is not None:
                for k, v in extra_env_vars.items():
                    run_env[k] = v

            # check if frozen
            env = dict(os.environ)  # make a copy of the environment
            lp_key = "LD_LIBRARY_PATH"  # for Linux and *BSD.
            lp_orig = env.get(lp_key + "_ORIG")  # pyinstaller >= 20160820 has this
            if lp_orig is not None:
                run_env[lp_key] = lp_orig  # restore the original, unmodified value
            else:
                run_env.pop(lp_key, None)  # last resort: remove the env var

            enc_key = token_urlsafe(32)

            self.process_secret_vars_vault(
                run_folder=run_folder,
                encryption_key=enc_key,
                sudo_password=sudo_password,
                ssh_password=ssh_password,
                secret_vars=secure_vars,
                elevated_permissions_required=elevated_permissions_required,
                run_env=run_env,
                passwordless_sudo_possible=passwordless_sudo_possible,
            )

            # write password file
            key_file = os.path.join(env_dir, "plays", "vault_pw")
            # local["touch"]([key_file])
            # print("TOUCHED: {}".format(key_file))
            with io.open(key_file, "w+") as fh:
                fh.write("")
            os.chmod(key_file, 0o600)
            with io.open(key_file, "w+") as fh:
                fh.write("{}".format(enc_key))

            # if sudo_password is None:
            proc = subprocess.Popen(
                script,
                stdout=subprocess.PIPE,
                stderr=sys.stdout.fileno(),
                stdin=subprocess.PIPE,
                shell=True,
                env=run_env,
                # preexec_fn=preexec_function,
                preexec_fn=os.setsid,
            )

            # proc.stdin.write(enc_key.encode(encoding="UTF-8"))
            # proc.stdin.close()

            for line in iter(proc.stdout.readline, ""):
                if line:
                    line = line.decode("utf-8").strip()
                    callback_adapter.add_log_message(line)
                if not line and proc.poll() is not None:
                    break

            while proc.poll() is None:
                # Process hasn't exited yet, let's wait some
                time.sleep(0.5)

            # Get return code from process
            return_code = proc.returncode
            parameters["return_code"] = return_code
            parameters["signal_status"] = -1

        except KeyboardInterrupt:
            cursor.show()  # looks like sometimes the cursor doesn't show otherwise...
            parameters["return_code"] = 11
            parameters["signal_status"] = -1

            # print()
            # print()
            # callback_adapter.add_error_message(
            #     "Keyboard interrupt received. Exiting..."
            # )
            # print()
            if proc is not None:
                os.killpg(os.getpgid(proc.pid), signal.SIGTERM)

            callback_adapter.cancel(
                "Keyboard interrupt received. Exiting. Already started tasks might or might not finish in the background..."
            )

        except (Exception) as e:

            if parameters is not None:
                parameters["return_code"] = 11
                parameters["signal_status"] = -1

            # import traceback

            # traceback.print_exc()
            # callback_adapter.add_error_message("Exception in Ansible run: {}".format(e))
            log.debug(e, exc_info=1)
            if proc is not None:
                os.killpg(os.getpgid(proc.pid), signal.SIGTERM)

            callback_adapter.cancel("Execution error: {}. Exiting...".format(e))
            raise e
        finally:
            callback_adapter.finish_up()

            if env_dir:
                run_vault_file = os.path.join(env_dir, "plays", "run_vault.yml")
                if os.path.exists(run_vault_file):
                    os.unlink(run_vault_file)
                vault_pw = os.path.join(env_dir, "plays", "vault_pw")
                if os.path.exists(vault_pw):
                    os.unlink(vault_pw)

        return {"nsbl_properties": parameters}
