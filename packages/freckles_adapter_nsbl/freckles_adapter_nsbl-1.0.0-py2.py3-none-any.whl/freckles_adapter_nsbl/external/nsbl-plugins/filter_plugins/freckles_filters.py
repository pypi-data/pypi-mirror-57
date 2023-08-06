# -*- coding: utf-8 -*-
# Copyright 2018 Markus Binsteiner <makkus@frkl.io>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
import os
import re

import yaml
from ansible.errors import AnsibleFilterError


class FilterModule(object):
    def filters(self):
        return {
            "very_basics_filter": self.box_very_basics_filter,
            "platform_var": self.platform_var_filter,
            "read_freckle_file_metadata": self.read_freckle_file_metadata,
            "read_directories_metadata": self.read_directory_metadata,
            "register_name_filter": self.register_name_filter,
            "register_var_filter": self.register_var_filter,
            "tasklist_path": self.get_tasklist_path,
            "select_python_interpreter": self.select_python_interpreter,
        }

    def select_python_interpreter(self, box_very_basics):

        if box_very_basics.get("python", None):
            return box_very_basics["python"]

        if box_very_basics.get("python_alt", None):
            return box_very_basics["python_alt"]

        return None

    def get_tasklist_path(self, tasklist_file_name, play_dir):

        tasklist_name = re.sub("[^0-9a-zA-Z_]", "_", tasklist_file_name)
        tasklist_name = re.sub("^[^a-zA-Z_]+", "_", tasklist_name)

        return os.path.realpath(
            os.path.join(
                play_dir, "..", "task_lists", "tasklist_{}".format(tasklist_name)
            )
        )

        return result

    def register_name_filter(self, register_name):

        register_name = str(register_name)
        tokens = register_name.split(".")

        return tokens[0]

    def register_var_filter(self, register_val, register_name):

        register_name = str(register_name)
        tokens = register_name.split(".")
        if len(tokens) == 1:
            return register_val

        last_token = tokens[-1]
        tokens = tokens[1:-1]

        result = {}
        current = result
        for token in tokens:
            current[token] = {}
            current = current[token]

        current[last_token] = register_val

        return result

    def read_directory_metadata(self, result_string):

        try:
            result = yaml.safe_load(result_string["stdout"])
        except (Exception) as e:
            raise AnsibleFilterError(
                "Error trying to parse box very basic facts: {}".format(e)
            )

        return result.get("directories", {})

    def read_freckle_file_metadata(self, result_string):

        try:
            result = yaml.safe_load(result_string["stdout"])
        except (Exception) as e:
            raise AnsibleFilterError(
                "Error trying to parse box very basic facts: {}".format(e)
            )

        freckle_files_dict = result.pop("freckle_files")
        dirs = {}
        for parent_path, f_files_dict in freckle_files_dict.items():
            freckle_files_invalid = {}
            freckle_files = {}
            for path, content in f_files_dict.items():
                if not content:
                    freckle_files[path] = {}
                    continue
                try:
                    c = yaml.safe_load(content)
                    freckle_files[path] = c
                except (Exception) as e:
                    freckle_files_invalid[path] = content

            dirs[parent_path] = {}
            dirs[parent_path]["freckle_files"] = freckle_files
            dirs[parent_path]["freckle_files_invalid"] = freckle_files_invalid

        return dirs

    def platform_var_filter(
        self, default_vars, platform_matchers, ignore_case=True, default_value=False
    ):
        """Computes the first matching variable out of a dict of variables (key: platform, value: var).
        """

        for platform in platform_matchers:

            if ignore_case:
                platform = platform.lower()

            for key, value in default_vars.items():
                if ignore_case:
                    key = key.lower()
                if key == platform:
                    return value

        return default_value

    def box_very_basics_filter(self, result_string):

        try:
            result = yaml.safe_load(result_string["stdout"])
        except (Exception) as e:
            raise AnsibleFilterError(
                "Error trying to parse box very basic facts: {}".format(e)
            )

        can_pwless_sudo = result.pop("can_passwordless_sudo")
        if can_pwless_sudo == 1 or can_pwless_sudo == 127:
            result["can_passwordless_sudo"] = False
        elif can_pwless_sudo == 0:
            result["can_passwordless_sudo"] = True
        else:
            raise AnsibleFilterError(
                "Invalid value for 'can_passwordless_sudo' key: {}".format(
                    can_pwless_sudo
                )
            )

        git_exes = result.pop("git_exes")
        if git_exes:
            git_xcode = result.pop("git_xcode")
            if git_xcode == 1:
                result["git_available"] = True
            elif git_xcode == 0:
                result["git_available"] = False
            else:
                raise AnsibleFilterError(
                    "Invalid value for 'git_xcode' key: {}".format(can_pwless_sudo)
                )
        else:
            result["git_available"] = False

        path = result.pop("path")
        paths = []
        for p in path.split(":"):
            if p:
                paths.append(p)
        result["path"] = paths

        freckle_files_dict = result.pop("freckle_files")
        dirs = {}
        for parent_path, f_files_dict in freckle_files_dict.items():
            freckle_files_invalid = {}
            freckle_files = {}
            for path, content in f_files_dict.items():
                if not content:
                    freckle_files[path] = {}
                    continue
                try:
                    c = yaml.safe_load(content)
                    freckle_files[path] = c
                except (Exception) as e:
                    freckle_files_invalid[path] = content

            dirs[parent_path] = {}
            dirs[parent_path]["freckle_files"] = freckle_files
            dirs[parent_path]["freckle_files_invalid"] = freckle_files_invalid
        result["freckle_files"] = dirs

        pythons_orig = result.pop("pythons")
        pythons = {}

        for python_exe, details in pythons_orig.items():

            if not details.get("exists", False):
                continue

            pythons[python_exe] = {}

            python_modules = details.pop("python_modules", None)
            missing_modules = []
            for m, exit_code in python_modules.items():
                if exit_code == 0:
                    continue

                missing_modules.append(m)
            pythons[python_exe]["missing_modules"] = missing_modules

        if len(pythons) == 0:
            result["install_python"] = True
        elif len(pythons) == 1:
            result["install_python"] = False
            result["python"] = list(pythons.keys())[0]
            result["missing_python_modules"] = pythons[result["python"]][
                "missing_modules"
            ]
        else:
            result["install_python"] = False
            best = None
            min = None
            # we prefer the virtualenv we created on localhost (because it contains all the python package requirements
            # for ansible modules
            for python, details in pythons.items():
                if not ".local/share/freckles" in python:
                    continue
                if best is None:
                    best = python
                    min = len(details["missing_modules"])
                    continue
                if len(details["missing_modules"]) < min:
                    best = python

            if best is None:
                best = None
                min = None
                for python, details in pythons.items():
                    if best is None:
                        best = python
                        min = len(details["missing_modules"])
                        continue
                    if len(details["missing_modules"]) < min:
                        best = python

            result["python"] = best
            result["missing_python_modules"] = pythons[result["python"]][
                "missing_modules"
            ]

        box_basics = result.pop("box_basics_file")
        ansible_python_interpreter = box_basics.get("python_interpreter", None)
        if ansible_python_interpreter is not None:
            result["python"] = ansible_python_interpreter
            result["install_python"] = False
            result["missing_python_modules"] = []

        pythons_alt_orig = result.pop("pythons_alt")
        python_alt = None
        for python_exe, details in pythons_alt_orig.items():

            if details.get("exists", False):
                python_alt = python_exe
                break

        result["python_alt"] = python_alt

        result["box_basics_version"] = box_basics.get("box_basics_version", 0)
        result["root_init_done"] = box_basics.get("root_init_done", False)

        return result
