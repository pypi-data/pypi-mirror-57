# -*- coding: utf-8 -*-

import copy
import getpass
import io
import json
import logging
import os
import shutil
from distutils.spawn import find_executable

from plumbum import local
from ruamel.yaml import YAML
from six import string_types

from freckles.adapters import FrecklesAdapter
from freckles.defaults import (
    EXTERNAL_FOLDER as FRECKLES_EXTERNAL_FOLDER,
    FRECKLET_KEY_NAME,
    VARS_KEY,
    FRECKLES_VENV_ENV_PATH,
    FRECKLES_CONDA_ENV_PATH,
    TASK_KEY_NAME,
    FRECKLES_CONDA_INSTALL_PATH,
)
from freckles.exceptions import FrecklesConfigException
from nsbl.defaults import (
    ADD_TYPE_FILES,
    ADD_TYPE_CALLBACK,
    ADD_TYPE_ACTION,
    ADD_TYPE_LIBRARY,
    ADD_TYPE_FILTER,
    ADD_TYPE_TASK_LIST_FILE,
)
from nsbl.nsbl import create_single_host_nsbl_env_from_tasklist
from nsbl.nsbl_tasklist import NsblContext
from nsbl.runner import NsblRunner

from frutils import readable_yaml
from .defaults import (
    NSBL_CONFIG_SCHEMA,
    NSBL_DEFAULT_FRECKLET_REPO,
    NSBL_EXTRA_CALLBACKS,
    NSBL_EXTRA_PLUGINS,
    NSBL_INTERNAL_TASKLIST_REPO,
    NSBL_RUN_CONFIG_SCHEMA,
    NSBL_DEFAULT_ROLE_REPO,
    NSBL_DEFAULT_TASKLIST_REPO,
    NSBL_COMMUNITY_FRECKLET_REPO,
    NSBL_COMMUNITY_ROLE_REPO,
    NSBL_COMMUNITY_TASKLIST_REPO,
)
from .nsbl_freckles_callback import NsblPrintCallbackAdapter


def create_yaml():
    yaml = YAML()
    yaml.default_flow_style = False
    yaml.preserve_quotes = True
    yaml.width = 4096
    return yaml


log = logging.getLogger("freckles")

ROLE_COPY_IGNORE_PATTERNS = ".git"

DEFAULT_ADDITIONAL_FILES = [
    {
        "path": os.path.join(FRECKLES_EXTERNAL_FOLDER, "scripts", "freckles_facts.sh"),
        "type": ADD_TYPE_FILES,
    },
    {
        "path": os.path.join(FRECKLES_EXTERNAL_FOLDER, "scripts", "freckle_folders.sh"),
        "type": ADD_TYPE_FILES,
    },
    {
        "path": os.path.join(NSBL_EXTRA_CALLBACKS, "default_to_file.py"),
        "type": ADD_TYPE_CALLBACK,
    },
    {
        "path": os.path.join(NSBL_EXTRA_CALLBACKS, "freckles_callback.py"),
        "type": ADD_TYPE_CALLBACK,
    },
    {
        "path": os.path.join(NSBL_EXTRA_PLUGINS, "action_plugins", "install.py"),
        "type": ADD_TYPE_ACTION,
    },
    {
        "path": os.path.join(NSBL_EXTRA_PLUGINS, "library", "install.py"),
        "type": ADD_TYPE_LIBRARY,
    },
    {
        "path": os.path.join(NSBL_EXTRA_PLUGINS, "library", "stow.py"),
        "type": ADD_TYPE_LIBRARY,
    },
    {
        "path": os.path.join(NSBL_EXTRA_PLUGINS, "library", "vagrant_plugin.py"),
        "type": ADD_TYPE_LIBRARY,
    },
    {
        "path": os.path.join(
            NSBL_EXTRA_PLUGINS, "action_plugins", "frecklet_result.py"
        ),
        "type": ADD_TYPE_ACTION,
    },
    {
        "path": os.path.join(NSBL_EXTRA_PLUGINS, "library", "frecklet_result.py"),
        "type": ADD_TYPE_LIBRARY,
    },
    {
        "path": os.path.join(
            NSBL_EXTRA_PLUGINS, "action_plugins", "set_platform_fact.py"
        ),
        "type": ADD_TYPE_ACTION,
    },
    {
        "path": os.path.join(NSBL_EXTRA_PLUGINS, "library", "set_platform_fact.py"),
        "type": ADD_TYPE_LIBRARY,
    },
    {
        "path": os.path.join(NSBL_EXTRA_PLUGINS, "library", "freckles_facts.py"),
        "type": ADD_TYPE_LIBRARY,
    },
    {
        "path": os.path.join(NSBL_EXTRA_PLUGINS, "action_plugins", "freckles_facts.py"),
        "type": ADD_TYPE_ACTION,
    },
    {
        "path": os.path.join(NSBL_EXTRA_PLUGINS, "library", "conda.py"),
        "type": ADD_TYPE_LIBRARY,
    },
    {
        "path": os.path.join(NSBL_EXTRA_PLUGINS, "library", "nix.py"),
        "type": ADD_TYPE_LIBRARY,
    },
    {
        "path": os.path.join(NSBL_EXTRA_PLUGINS, "library", "asdf.py"),
        "type": ADD_TYPE_LIBRARY,
    },
    # {
    #     "path": os.path.join(NSBL_EXTRA_PLUGINS, "module_utils", "freckles_utils.py"),
    #     "type": ADD_TYPE_MODULE_UTIL,
    # },
    # {
    #     "path": os.path.join(NSBL_ROLES, "package-management", "freckfrackery.install"),
    #     "type": ADD_TYPE_ROLE,
    # },
    # {
    #     "path": os.path.join(NSBL_ROLES, "package-management", "freckfrackery.install-pkg-mgrs"),
    #     "type": ADD_TYPE_ROLE,
    # },
    {
        "path": os.path.join(
            NSBL_EXTRA_PLUGINS, "filter_plugins", "freckles_filters.py"
        ),
        "type": ADD_TYPE_FILTER,
    },
    {
        "path": os.path.join(NSBL_INTERNAL_TASKLIST_REPO, "box_basics.yml"),
        "type": ADD_TYPE_TASK_LIST_FILE,
    },
    {
        "path": os.path.join(NSBL_INTERNAL_TASKLIST_REPO, "box_basics_root.yml"),
        "type": ADD_TYPE_TASK_LIST_FILE,
    },
    {
        "path": os.path.join(NSBL_INTERNAL_TASKLIST_REPO, "freckles_basic_facts.yml"),
        "type": ADD_TYPE_TASK_LIST_FILE,
    },
]


def generate_pre_tasks(
    minimal_facts=True, box_basics=True, box_basics_non_sudo=False, freckles_facts=True
):
    """Generates a list of tasks that will end up in a playbooks pre_tasks variable.

    Args:
        minimal_facts (bool): whether to run a basic shell script to gather some basic facts (this doesn't require Python on the target machine, but can find out whether Python is available.
        box_basics (bool): whether to install a minimal set to be able to run common Ansible modules on this machine
        box_basics_non_sudo (bool): whether to run the 'non-sudo' version of box basics (not implemented yet)
        freckles_facts (bool): whether to run the freckles facts module

    Returns:
        tuple: a tuple in the form: (task_list, gather_facts_included), gather_facts_included indicates whether the pre_tasks will run gather_facts at some stage (so it doesn't need to be executed twice.
    """

    gather_facts_included = False
    pre_tasks = []

    # check_script_location = os.path.join(
    #     "{{ playbook_dir }}", "..", "files", "freckles_facts.sh"
    # )

    # TODO: this doesn't really do anything at the moment, vars are hardcoded in freckles_facts.sh
    # check_executables = [
    #     "cat",
    #     "wget",
    #     "curl",
    #     "python",
    #     "python2",
    #     "python2.7",
    #     "python3",
    #     "python3.6",
    #     "vagrant",
    #     "pip",
    #     "conda",
    #     "nix",
    #     "asdf",
    #     "rsync",
    # ]
    # check_python_modules = ["zipfile"]
    # pre_path = []
    # post_path = []
    # check_freckle_files = []
    # check_directories = []
    # freckles_facts_environment = (
    #     {
    #         "FRECKLES_CHECK_EXECUTABLES": ":".join(check_executables),
    #         "FRECKLES_CHECK_DIRECTORIES": ":".join(check_directories),
    #         "FRECKLES_PRE_PATH": ":".join(pre_path),
    #         "FRECKLES_POST_PATH": ":".join(post_path),
    #         "FRECKLES_CHECK_FRECKLE_FILES": ":".join(check_freckle_files),
    #         "FRECKLES_CHECK_PYTHON_MODULES": ":".join(check_python_modules),
    #     },
    # )

    if minimal_facts or box_basics or freckles_facts:
        temp = [
            {
                "name": "[-1000][testing connectivity]",
                "raw": 'sh -c "true"',
                "ignore_errors": False,
                "changed_when": False,
            },
            # {
            #     "name": "[-1000][checking whether box already prepared]",
            #     "raw": 'sh -c "test -e $HOME/.local/share/freckles/.box_basics && echo 1 || echo 0"',
            #     "ignore_errors": True,
            #     "register": "box_basics_exists",
            # },
            # {
            #     "name": "[setting box_basics var]",
            #     "set_fact": {
            #         "box_basics": "{{ box_basics_exists.stdout_lines[0] | bool }}",
            #         "freckles_environment": freckles_facts_environment,
            #     },
            # },
            {
                "name": "[getting box basic facts]",
                "include_tasks": "{{ playbook_dir }}/../task_lists/freckles_basic_facts.yml",
            },
        ]
        pre_tasks.extend(temp)

    if box_basics or freckles_facts:

        gather_facts_included = True
        temp = [
            {
                "name": "[preparing box basics]",
                "include_tasks": "{{ playbook_dir }}/../task_lists/box_basics.yml",
                # "when": "not box_very_basics['root_init_done']",
            },
            # {
            #     "name": "[gathering facts]",
            #     "setup": {},
            #     "tags": "always",
            #     "when": "box_very_basics['root_init_done']",
            # },
        ]
        pre_tasks.extend(temp)

    if freckles_facts:

        pre_tasks.append(
            {
                "name": "[gathering freckles-specific facts]",
                "freckles_facts": {"executables": ["unzip"]},
            }
        )

    return {"pre_tasks": pre_tasks, "gather_facts": not gather_facts_included}


def generate_additional_files_dict():

    additional_files = {}

    for f in DEFAULT_ADDITIONAL_FILES:

        path = f["path"]
        if not os.path.exists(path):
            raise FrecklesConfigException("File '{}' not available".format(path))

        f_type = f["type"]
        target_name = f.get("target_name", os.path.basename(path))

        additional_files[path] = {"type": f_type, "target_name": target_name}

        license_path = path + ".license"
        if os.path.exists(license_path):
            target_name_license = target_name + ".license"
            additional_files[license_path] = {
                "type": f["type"],
                "target_name": target_name_license,
            }

    return additional_files


class FrecklesAdapterNsbl(FrecklesAdapter):
    def __init__(self, name, context):

        super(FrecklesAdapterNsbl, self).__init__(
            adapter_name=name,
            context=context,
            config_schema=NSBL_CONFIG_SCHEMA,
            run_config_schema=NSBL_RUN_CONFIG_SCHEMA,
        )

        self._nsbl_context = None

    def get_resources_for_task(self, task):

        # output(task, output_type="yaml")

        role_paths = []
        if task[FRECKLET_KEY_NAME]["type"] == "ansible-role":
            role_name = task[TASK_KEY_NAME]["command"]
            path = self.nsbl_context.get_role_path(role_name)
            role_paths.append(path)

        roles = task.get(TASK_KEY_NAME, {}).get("roles", [])

        for role_name in roles:
            path = self.nsbl_context.get_role_path(role_name)
            if path not in role_paths:
                role_paths.append(path)

        tasklist_paths = []
        if task[FRECKLET_KEY_NAME]["type"] == "ansible-tasklist":
            tasklist_name = task[TASK_KEY_NAME]["command"]
            path = self.nsbl_context.get_tasklist(tasklist_name)
            tasklist_paths.append(path)

        tasklists = task.get(TASK_KEY_NAME, {}).get("ansible-tasklists", [])
        for tasklist_name in tasklists:
            path = self.nsbl_context.get_tasklist(tasklist_name)
            if path not in tasklist_paths:
                tasklist_paths.append(path)

        return {"roles": role_paths, "ansible-tasklists": tasklist_paths}

    def get_lookup_plugin_requirements(self, tasklist):

        result = []

        plugin_dep_map = {
            "aws_account_attribute": ["boto3", "botocore"],
            "aws_secret": ["boto3", "botocore>=1.10.0"],
            "aws_ssm": ["boto3", "botocore"],
            "chef_databag": ["pychef"],
            "consul_kv": ["python-consul"],
            "credstash": ["credstash"],
            "dig": ["dnspython"],
            "dnstxt": ["dnspython"],
            "hashi_vault": ["hvac"],
            "k8s": ["openshift>0.6"],
            "keyring": ["keyring"],
            "laps_password": ["python-ldap"],
            "mongodb": ["pymongo>=2.4"],
            "rabbitmq": ["pika"],
            "redis": ["redis-py"],
            "skydive": ["skydive-client"],
        }

        non_python_deps = {
            "cyberarkpassword",
            "hiera",
            "lastpass",
            "nios",
            "nios_next_ip",
            "nios_next_network",
            "onepassword",
            "onepassword_raw",
        }

        for lookup in non_python_deps:
            if (
                "lookup('{}".format(lookup) in tasklist
                or 'lookup("{}'.format(lookup) in tasklist
            ):
                log.warning(
                    "Lookup '{}' found, which needs external dependencies. Please make sure you installed them manually before this run.".format(
                        lookup
                    )
                )

        for lookup, dep in plugin_dep_map.items():

            if (
                "lookup('{}".format(lookup) in tasklist
                or 'lookup("{}'.format(lookup) in tasklist
            ):
                for d in dep:
                    if d not in result:
                        result.append(d)

        return result

    def prepare_execution_requirements(self, run_config, task_list, parent_task):

        frkl_pkg = self.context.frkl_pkg

        ansible_exe = find_executable(
            "ansible-playbook",
            path=":".join(
                frkl_pkg.lookup_paths(incl_system_path=False, include_frozen=False)
            ),
        )

        ansible_version = self.run_config_value("ansible_version")
        force_ansible_version = self.run_config_value("force_ansible_version")

        if ansible_exe:
            # TODO: check whether ansible version matches configured one
            # Test whether it works, could be a pyenv shim
            a_ex = local[ansible_exe]

            works = False
            try:
                rc, stdout, stderr = a_ex.run(["--version"])
                works = rc == 0
                if works and force_ansible_version:
                    works = stdout.startswith(
                        "ansible-playbook {}".format(ansible_version)
                    )
            except (Exception) as e:
                log.warning(
                    "Can't use existing Ansible ( {} ), trying to install (again)...".format(
                        e
                    )
                )
                pass

            if not works:
                ansible_exe = None

        package_list = []
        if not ansible_exe:
            package_list.append("ansible=={}".format(ansible_version))
            package_list.append("jmespath")

        if self.run_config_value("use_ara"):
            package_list.append("ara[server]")

        for task in task_list:

            pip_dpendencies = (
                task.get(FRECKLET_KEY_NAME, {})
                .get("resources", {})
                .get("python-package", [])
            )
            package_list.extend(pip_dpendencies)

        # check lookup plugins
        task_list_string = readable_yaml(task_list, ignore_aliases=True, safe=False)

        if "lookup(" in task_list_string:
            req = self.get_lookup_plugin_requirements(task_list_string)
            package_list.extend(req)

        if package_list:

            package_list = list(set(package_list))

            prepare_task = parent_task.add_subtask(
                task_name="preparing execution environment",
                msg="preparing execution environment",
                category="adapter_prepare",
            )

            frkl_pkg.ensure_python_packages(
                package_list=package_list,
                allow_current=False,
                venv_path=FRECKLES_VENV_ENV_PATH,
                conda_path=FRECKLES_CONDA_ENV_PATH,
                conda_install_path=FRECKLES_CONDA_INSTALL_PATH,
                env_type="auto",
                parent_task=prepare_task,
                system_site_packages=True,
                update_packages=True,
            )

            prepare_task.finish()

    @property
    def nsbl_context(self):
        """Calculate the context from the available repositories and config."""

        if self._nsbl_context is None:
            role_repos = self.resource_folder_map.get("ansible-role", [])
            tasklist_repos = self.resource_folder_map.get("ansible-tasklist", [])
            urls = {}
            role_paths = []
            for rr in role_repos:
                path = rr["path"]
                if path not in role_paths:
                    role_paths.append(path)
            urls["roles"] = role_paths
            tasklist_paths = []
            for tlr in tasklist_repos:
                path = tlr["path"]
                if path not in tasklist_paths:
                    tasklist_paths.append(path)
            urls["tasklists"] = tasklist_paths

            try:
                allow_remote = self.config_value("allow_remote")
            except (Exception):
                allow_remote = False
            try:
                allow_remote_roles = self.config_value("allow_remote_roles")
            except (Exception):
                allow_remote_roles = False
            try:
                allow_remote_tasklists = self.config_value("allow_remote_tasklists")
            except (Exception):
                allow_remote_tasklists = False

            if allow_remote_roles is None:
                allow_remote_roles = allow_remote
            if allow_remote_tasklists is None:
                allow_remote_tasklists = allow_remote

            self._nsbl_context = NsblContext(
                urls=urls,
                allow_external_roles=allow_remote_roles,
                allow_external_tasklists=allow_remote_tasklists,
            )

        return self._nsbl_context

    # def get_config_schema(self):
    #
    #     return NSBL_CONFIG_SCHEMA
    #
    # def get_run_config_schema(self):
    #
    #     return NSBL_RUN_CONFIG_SCHEMA

    def get_folders_for_alias(self, alias):

        if alias == "default":

            return [
                "frecklet::{}".format(NSBL_DEFAULT_FRECKLET_REPO),
                "ansible-role::{}".format(NSBL_DEFAULT_ROLE_REPO),
                "ansible-tasklist::{}".format(NSBL_DEFAULT_TASKLIST_REPO),
            ]

        elif alias == "community":

            return [
                "frecklet::{}".format(NSBL_COMMUNITY_FRECKLET_REPO),
                "ansible-role::{}".format(NSBL_COMMUNITY_ROLE_REPO),
                "ansible-tasklist::{}".format(NSBL_COMMUNITY_TASKLIST_REPO),
            ]

        else:
            return []

    def get_supported_resource_types(self):

        return ["ansible-role", "ansible-tasklist"]

    def get_supported_task_types(self):

        return ["ansible-module", "ansible-role", "ansible-tasklist", "ansible-meta"]

    def process_secure_vars_environment(self, task):

        secure_vars = {}

        force_log = self.config_value("force_show_log")
        task_id = task[FRECKLET_KEY_NAME]["_task_id"]
        secret_task_vars = task[FRECKLET_KEY_NAME]["secret_vars"]

        for var_name, var_value in task.get(VARS_KEY, {}).items():
            if var_name not in secret_task_vars:
                continue
            var_alias = "task_{}_pw_{}".format(task_id, var_name)

            if isinstance(var_value, string_types):
                val = var_value
                repl = "{{{{ lookup('env', '{}') }}}}".format(var_alias)
            else:
                val = json.dumps(var_value)
                repl = "{{{{ lookup('env', '{}') | from_json }}}}".format(var_alias)

            secure_vars[var_alias] = {"type": "environment", "value": val}
            task[VARS_KEY][var_name] = repl
            if not force_log:
                task["task"]["no_log"] = True

        return secure_vars

    def process_secure_vars_vault(self, task):

        secure_vars = {}

        force_log = self.config_value("force_show_log")
        task_id = task[FRECKLET_KEY_NAME]["_task_id"]
        secret_task_vars = task[FRECKLET_KEY_NAME]["secret_vars"]

        for var_name, var_value in task.get(VARS_KEY, {}).items():
            if var_name not in secret_task_vars:
                continue

            secret_var_name = "__secret_task_{}_{}__".format(task_id, var_name)
            secure_vars[secret_var_name] = var_value
            repl = "{{{{ {} }}}}".format(secret_var_name)
            task[VARS_KEY][var_name] = repl
            if not force_log:
                task["task"]["no_log"] = True

        return secure_vars

    def copy_resource(self, resource_name, resource_type, dest_path):

        if resource_type == "ansible-module":
            return True
        elif resource_type == "ansible-tasklist":
            content = self.nsbl_context.get_tasklist(resource_name)

            tasklist_dest_path = os.path.join(dest_path, resource_name)
            log.debug("Render 'ansible-tasklist': {}".format(tasklist_dest_path))

            with io.open(tasklist_dest_path, "w", encoding="utf-8") as tlf:
                yaml = create_yaml()
                yaml.dump(content, tlf)

            return True
        elif resource_type == "ansible-role":

            path = self.nsbl_context.get_role_path(resource_name)
            role_dest_path = os.path.join(dest_path, resource_name)

            if os.path.exists(role_dest_path):
                # we assume the resources are identical
                return True

            shutil.copytree(
                src=path,
                dst=role_dest_path,
                ignore=shutil.ignore_patterns(ROLE_COPY_IGNORE_PATTERNS),
            )

            return True

    def run(
        self,
        tasklist,
        run_vars,
        run_config,
        run_secrets,
        run_env,
        result_callback,
        parent_task,
    ):

        if parent_task is None:
            raise Exception("No parent task provided")

        minimal_facts_only = run_config["minimal_facts_only"]

        if minimal_facts_only:
            pre_tasks = generate_pre_tasks(
                minimal_facts=True,
                box_basics=False,
                box_basics_non_sudo=False,
                freckles_facts=False,
            )
        else:
            pre_tasks = generate_pre_tasks(
                minimal_facts=True,
                box_basics=True,
                box_basics_non_sudo=False,
                freckles_facts=True,
            )
        additional_files = generate_additional_files_dict()

        final_config = copy.deepcopy(run_config)

        # check connection
        u = final_config.get("user")
        h = final_config.get("host")
        current_user = getpass.getuser()
        if h == "127.0.0.1" or h == "localhost":
            if (
                u
                and current_user != u
                and final_config.get("connection_type", None) != "ssh"
            ):
                log.warning(
                    "Using localhost as target, but different user, changing connection type to 'ssh'. Make sure that is what you want."
                )
                final_config["connection_type"] = "ssh"

        # adding execution path

        nsbl_run_dir = os.path.join(run_env["env_dir"], "nsbl")

        final_config["add_symlink_to_env"] = False
        final_config["add_timestamp_to_env"] = False
        final_config["force"] = False
        final_config["run_folder"] = nsbl_run_dir

        secure_vars = {}

        tasklist_new = []

        for task in tasklist:

            if task[FRECKLET_KEY_NAME]["type"] == "ansible-meta":
                new_task = copy.deepcopy(task)
                vars = new_task.pop(VARS_KEY)
                f_type = task[FRECKLET_KEY_NAME]["name"]
                module_name = vars["name"]
                vars_vars = vars.get("vars", {})

                new_task[FRECKLET_KEY_NAME]["type"] = f_type
                new_task[FRECKLET_KEY_NAME]["name"] = module_name
                new_task[TASK_KEY_NAME]["command"] = module_name
                new_task[VARS_KEY] = vars_vars

                task = new_task

            tasklist_new.append(task)

            secure_vars_task = self.process_secure_vars_vault(task)
            secure_vars.update(secure_vars_task)

        # run_resources = run_env["resource_path"]
        # urls = {
        #     "ansible-tasklists": os.path.join(run_resources, "ansible-tasklists"),
        #     "roles": os.path.join(run_resources, "roles"),
        # }
        # run_nsbl_context = NsblContext(
        #     urls=urls,
        #     allow_external_roles=self.nsbl_context.allow_external_roles,
        #     allow_external_tasklists=self.nsbl_context.allow_external_tasklists,
        # )
        run_nsbl_context = self.nsbl_context

        nsbl_env = create_single_host_nsbl_env_from_tasklist(
            tasklist_new,
            run_nsbl_context,
            pre_tasks=pre_tasks["pre_tasks"],
            gather_facts=pre_tasks["gather_facts"],
            additional_files=additional_files,
            global_task_vars=result_callback.result,
            task_marker="task",
            meta_marker="frecklet",
            **final_config
        )

        # callback_adapter = NsblFrecklesCallbackAdapter(
        #     nsbl_env, parent_task=parent_task, result_callback=result_callback
        # )
        final_config["callback"] = "freckles_callback"
        callback_adapter = NsblPrintCallbackAdapter(
            root_task=parent_task, result_callback=result_callback
        )
        # callback_adapter = NsblFrecklesCallbackAdapter(nsbl=nsbl_env, parent_task=parent_task, result_callback=result_callback)

        sudo_password = run_secrets.get("become_pass", None)
        ssh_password = run_secrets.get("login_pass", None)

        extra_env_vars = {}
        if "pwd" in run_vars["__freckles_run__"].keys():
            extra_env_vars["NSBL_RUN_PWD"] = run_vars["__freckles_run__"]["pwd"]

        nsbl_runner = NsblRunner(nsbl_env)

        result = nsbl_runner.run(
            callback_adapter=callback_adapter,
            sudo_password=sudo_password,
            ssh_password=ssh_password,
            extra_env_vars=extra_env_vars,
            secure_vars=secure_vars,
            extra_paths=reversed(
                self.context.frkl_pkg.lookup_paths(
                    incl_system_path=False, include_frozen=False
                )
            ),
            parent_task=parent_task,
            **final_config
        )

        return result
