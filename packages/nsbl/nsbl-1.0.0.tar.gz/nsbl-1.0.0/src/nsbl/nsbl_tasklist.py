# -*- coding: utf-8 -*-

# python 3 compatibility
from __future__ import absolute_import, division, print_function, unicode_literals

import copy
import logging
import os
from collections import Mapping

from ruamel.yaml.comments import CommentedMap
from six import string_types

from frkl import Frklist, FrklistContext, load_object_from_url_or_path
from frutils import StringYAML, is_url_or_abbrev
from frutils.exceptions import FrklException
from frutils.frutils import valid_python_var_name
from .defaults import (
    ADD_TYPE_ROLE,
    ADD_TYPE_TASK_LIST,
    DEFAULT_INCLUDE_TYPE,
    FRECKLES_DESC_METADATA_KEY,
    FRECKLES_DESC_SHORT_METADATA_KEY,
)
from .exceptions import NsblException
from .role_utils import find_roles_in_repos
from .tasklist_utils import ANSIBLE_TASK_KEYWORDS, find_tasklists_in_repos

GLOBAL_ENV_ID_COUNTER = 1110
GLOBAL_TASKLIST_ID_COUNTER = 1110


def GLOBAL_TASKLIST_ID():
    global GLOBAL_TASKLIST_ID_COUNTER
    GLOBAL_TASKLIST_ID_COUNTER = GLOBAL_TASKLIST_ID_COUNTER + 1
    return GLOBAL_TASKLIST_ID_COUNTER


def GLOBAL_ENV_ID():
    global GLOBAL_ENV_ID_COUNTER
    GLOBAL_ENV_ID_COUNTER = GLOBAL_ENV_ID_COUNTER + 1
    return GLOBAL_ENV_ID_COUNTER


yaml = StringYAML()
yaml.default_flow_style = False

log = logging.getLogger("nsbl")


class NsblContext(FrklistContext):
    def __init__(
        self, allow_external_roles=None, allow_external_tasklists=None, **kwargs
    ):
        super(NsblContext, self).__init__(**kwargs)

        if allow_external_roles is None:
            allow_external_roles = self.allow_remote
        self.allow_external_roles = allow_external_roles

        if allow_external_tasklists is None:
            allow_external_tasklists = self.allow_remote
        self.allow_external_tasklists = allow_external_tasklists

        self.role_repo_paths = self.urls.get("roles", [])
        self.tasklist_paths = self.urls.get("tasklists", [])

        self.available_roles, all_role_paths = find_roles_in_repos(self.role_repo_paths)
        self.available_tasklists, self.tasklists_per_repo = find_tasklists_in_repos(
            self.tasklist_paths, exclude_paths=all_role_paths
        )  # we don't want tasklists from any roles

    def get_role_path(self, role_name):

        if role_name in self.available_roles.keys():
            return self.available_roles[role_name]
        else:
            if self.allow_external_roles:
                return role_name
            else:
                raise Exception(
                    "External roles not allowed, and role '{}' not in role paths: {}".format(
                        role_name, self.role_repo_paths
                    )
                )

    def get_tasklist(self, tasklist_name):

        if tasklist_name in self.available_tasklists.keys():
            return self.available_tasklists[tasklist_name]
        else:

            if os.path.exists(tasklist_name):
                return load_object_from_url_or_path(tasklist_name)
            elif is_url_or_abbrev(tasklist_name):
                if not self.allow_external_tasklists or self.allow_remote:
                    raise Exception(
                        "Remote tasklist not allowed, not retrieving: {}".format(
                            tasklist_name
                        )
                    )
                try:
                    return load_object_from_url_or_path(tasklist_name)
                except (Exception) as e:
                    raise Exception(
                        "Could not download tasklist '{}': {}".format(tasklist_name, e)
                    )
            else:
                raise Exception(
                    "Could not find Ansible tasklist '{}' in tasklist paths: {}".format(
                        tasklist_name, self.tasklist_paths
                    )
                )

    def get_repo_for_tasklist(self, tasklist_name):

        for repo, tlns in self.tasklists_per_repo.items():

            if tasklist_name in tlns:
                return repo

        return None


class NsblTasklist(Frklist):
    def __init__(
        self,
        itemlist,
        context,
        meta=None,
        vars=None,
        task_marker="task",
        meta_marker="task",
    ):

        if not isinstance(context, NsblContext):
            raise Exception("Context needs to be of type NsblContext")

        self.internal_roles = set()
        self.external_roles = set()
        self.modules_used = set()
        self.tasklist_files = {}
        self.children = []
        self.additional_files = {}

        self.task_lookup = {}

        self.task_marker = task_marker
        self.meta_marker = meta_marker

        super(NsblTasklist, self).__init__(itemlist, context, meta=meta, vars=vars)

    def expand_and_augment_tasklist(self, tasklist):

        result = []
        for task in tasklist:

            index = task[self.meta_marker]["_task_id"]

            self.task_lookup[index] = task

            name = task[self.meta_marker].get("name", None)
            command = task[self.task_marker].get("command", None)
            if name is None:
                if command is None:
                    raise Exception(
                        "Task doesn't have 'name' nor 'command' key: {}".format(task)
                    )
                name = command
                task[self.meta_marker]["name"] = command
            if command is None:
                command = name
                task[self.task_marker]["command"] = command
            temp = {
                self.task_marker: copy.deepcopy(task[self.task_marker]),
                "vars": task.get("vars", {}),
            }

            task_type = task[self.meta_marker]["type"]
            temp[self.task_marker]["type"] = task_type

            desc_val = task.get(self.meta_marker, {}).get(
                FRECKLES_DESC_METADATA_KEY, {}
            )
            msg = desc_val.get(
                FRECKLES_DESC_SHORT_METADATA_KEY, "{}: {}".format(task_type, command)
            )

            if msg is None:
                msg = task.get("doc", {}).get("msg", None)

            if msg is not None:
                temp[self.task_marker]["name"] = "[{}] {}".format(index, msg)
            else:
                temp[self.task_marker]["name"] = "[{}] {}".format(index, name)

            if temp[self.task_marker]["type"] == "ansible-role":

                if "include-type" not in temp[self.task_marker].keys():
                    temp[self.task_marker]["include-type"] = DEFAULT_INCLUDE_TYPE

                temp.setdefault("vars", {})["_task_id"] = index

                if "role_path" in temp[self.task_marker].keys():
                    path = temp[self.task_marker]["role_path"]
                else:
                    path = self.context.get_role_path(command)
                    temp[self.task_marker]["role_path"] = path

                self.add_role_to_addition_files(command, path=path)

            if temp[self.task_marker]["type"] == "ansible-tasklist":
                include_type = temp[self.task_marker].get("include-type", None)
                if include_type is None:
                    include_type = DEFAULT_INCLUDE_TYPE
                    temp[self.task_marker]["include-type"] = include_type

                temp.setdefault("vars", {})["_task_id"] = index

                tasklist_var = temp[self.task_marker].get("tasklist_var", None)
                if tasklist_var is None:
                    tasklist_var = "tasklist_{}".format(command)

                tasklist_var = valid_python_var_name(tasklist_var)
                temp[self.task_marker]["tasklist_var"] = tasklist_var

                self.add_tasklist_to_additional_files(command, tasklist_var)

            # resources
            resources = task[self.meta_marker].get("resources", {})

            for res_type, res_urls in resources.items():
                if res_type == "ansible-module":
                    # no need to do anything, as those are included
                    continue
                if res_type not in ["ansible-role", "ansible-tasklist"]:
                    continue

                if res_type == "ansible-role":
                    roles = res_urls
                    if isinstance(roles, string_types):
                        roles = [roles]

                    for role in roles:
                        self.add_role_to_addition_files(role, path=None)

                elif res_type == "ansible-tasklist":

                    tasklists = res_urls
                    if isinstance(tasklists, string_types):
                        tasklists = [tasklists]

                    for tl_name in tasklists:

                        tasklist_var = "tasklist_{}".format(tl_name)

                        tasklist_var = valid_python_var_name(tasklist_var)
                        task[self.task_marker]["tasklist_var"] = tasklist_var
                        self.add_tasklist_to_additional_files(tl_name, tasklist_var)

            result.append(temp)

            # moving 'register' value to 'task' key
            reg_val = task[self.meta_marker].get("register", None)
            if not reg_val:
                continue
            if not isinstance(reg_val, Mapping):
                raise TypeError(
                    "'register' value must be a mapping type: {}".format(reg_val)
                )
            temp.setdefault(self.task_marker, {})["register"] = reg_val

            # import pp, sys
            # pp(reg_val)
            # sys.exit()
            #
            # if (
            #     reg_val is not None
            #     and isinstance(reg_val, string_types)
            #     or (isinstance(reg_val, Mapping) and "var" in reg_val.keys())
            # ):
            #
            #     register_val = task[self.meta_marker]["register"]
            #     if isinstance(register_val, string_types):
            #         register_name = register_val
            #         register_query = None
            #     elif isinstance(register_val, Mapping):
            #         if "var" in register_val.keys():
            #
            #             register_name = register_val["var"]
            #             register_query = register_val.get("query", None)
            #
            #     if (
            #         "register" in temp[self.task_marker].keys()
            #         and temp[self.task_marker]["register"] != register_name
            #     ):
            #         t = copy.deepcopy(task)
            #         t[self.meta_marker].pop("secret_vars", None)
            #         t[self.meta_marker].pop("_task_id", None)
            #         raise FrklException(
            #             msg="Different 'register' values specified in both '{}' and '{}' subkeys".format(
            #                 self.task_marker, self.meta_marker
            #             ),
            #             solution="Check your task description for this task:\n\n{}\n\nEither remove one of the 'register' keys, or make sure they both have the same value.".format(
            #                 readable_yaml(t, indent=4)
            #             ),
            #         )
            #
            #     rn = register_name
            #     # TODO: check for other special characters
            #     if "-" in rn:
            #         t = copy.deepcopy(task)
            #         t[self.meta_marker].pop("secret_vars", None)
            #         t[self.meta_marker].pop("_task_id", None)
            #         raise FrklException(
            #             msg="Invalid 'register' keyname '{}', must be a valid variable name (can't contain '-', special charcters...)".format(
            #                 rn
            #             ),
            #             solution="Check your task description for this task:\n\n{}\n\nChange the 'register' variable name ('{}') to not contain any special characters.".format(
            #                 readable_yaml(t, indent=4), rn
            #             ),
            #         )
            #
            #     temp[self.task_marker]["register"] = rn
            #     if register_query is not None:
            #         temp[self.task_marker]["register_query"] = register_query

        return result

    def get_task(self, index):

        return self.task_lookup.get(index, None)

    def render_tasklist(self, secure_vars=None, show_tasks_with_password_in_log=False):
        """Renders the playbook into a file."""

        result = []

        for t in self.itemlist:

            task = copy.deepcopy(t)
            log.debug("Task item: {}".format(task))
            name = task[self.task_marker].pop("name")
            command = task[self.task_marker].pop("command", None)
            task_type = task[self.task_marker].pop("type")
            desc_val = task[self.task_marker].pop(FRECKLES_DESC_METADATA_KEY, {})
            desc = desc_val.get(FRECKLES_DESC_SHORT_METADATA_KEY, None)
            # legacy
            task_desc = task[self.task_marker].pop("task-desc", None)
            if desc is None:
                desc = task_desc
            if desc is None:
                desc = name

            vars = CommentedMap()
            task_has_password = False

            for key, value in task.pop("vars").items():

                # for alias in secure_vars.keys():
                #
                #     pw_wrap_method = secure_vars[alias]["type"]
                #     if pw_wrap_method != "environment":
                #         raise NsblException(
                #             "Password-wrap method '{}' not supported in nsbl.".format(
                #                 pw_wrap_method
                #             )
                #         )
                #     value, changed = simple_replace_string_in_obj(
                #         value, alias, "{{{{ lookup('env', '{}') }}}}".format(alias)
                #     )
                #     if changed:
                #         task_has_password = True

                vars[key] = value

            task_item = CommentedMap()
            task_item["name"] = desc

            if task_type == "ansible-module":
                if command is None:
                    raise NsblException(
                        "No 'command' key specified in task: {}".format(task)
                    )
                if "free_form" in vars.keys():
                    temp = copy.deepcopy(vars)
                    free_form = temp.pop("free_form")
                    task_item[command] = free_form
                    task_item["args"] = temp
                else:
                    task_item[command] = vars
            elif task_type == "ansible-tasklist":
                include_type = task[self.task_marker]["include-type"]
                task_key = "{}_tasks".format(include_type)
                task_item[task_key] = "{{{{ {} }}}}".format(
                    task[self.task_marker]["tasklist_var"]
                )
                task_item["vars"] = vars
                if include_type == "include":
                    b = task.get("task", {}).pop("become", None)
                    if b is not None:
                        task_item["vars"].setdefault("apply", {})["become"] = b
                    bu = task.get("task", {}).pop("become_user", None)
                    if bu is not None:
                        task_item["vars"].setdefault("apply", {})["become_user"] = bu

            elif task_type == "ansible-role":
                if command is None:
                    raise NsblException(
                        "No 'command' key specified in task: {}".format(task)
                    )
                include_type = task[self.task_marker]["include-type"]
                task_key = "{}_role".format(include_type)
                task_item[task_key] = {"name": command}
                task_item["vars"] = vars

                if include_type == "include":
                    b = task.get("task", {}).pop("become", None)
                    if b is not None:
                        task_item["vars"].setdefault("apply", {})["become"] = b
                    bu = task.get("task", {}).pop("become_user", None)
                    if bu is not None:
                        task_item["vars"].setdefault("apply", {})["become_user"] = bu

                for additional in [
                    "allow_duplicates",
                    "defaults_from",
                    "tasks_from",
                    "vars_from",
                ]:
                    value = task[self.task_marker].get(additional, None)
                    if value is not None:
                        task_item[task_key][additional] = value

            # add the remaining key/value pairs
            unknown_keys = []
            for key, value in task[self.task_marker].items():
                if key in ANSIBLE_TASK_KEYWORDS:
                    task_item[key] = value
                else:
                    unknown_keys.append(key)

            if task_has_password and not show_tasks_with_password_in_log:
                if "no_log" not in task_item.keys():
                    task_item["no_log"] = True

            # adding 'skip' conditions
            skip_internal_list = t[self.task_marker].get("__skip_internal__", [])
            if skip_internal_list:
                when_list = []
                when = task_item.get("when", None)
                if when:
                    when_list.append("( {} )".format(when))
                for skip_item in skip_internal_list:
                    when_list.append("( not {} )".format(skip_item))

                when_string = " and ".join(when_list)
                task_item["when"] = when_string

            result.append(task_item)

            reg_val = task_item.pop("register", None)
            if not reg_val:
                continue

            if not isinstance(reg_val, Mapping):
                temptask = copy.copy(task_item)
                temptask["register"] = reg_val
                raise FrklException(
                    msg="Can't parse task: {}".format(dict(temptask)),
                    reason="Invalid type for 'register' value: {}".format(
                        type(reg_val)
                    ),
                    solution="Use a mapping.",
                )

            register_var_name = reg_val["id"]
            task_item["register"] = register_var_name
            register_task = {
                "name": "[freckles register variable: {}]".format(register_var_name),
                "debug": {"msg": "{{{{ {} }}}}".format(register_var_name)},
            }
            result.append(register_task)

            # sys.exit()
            # if (
            #     "register" in task_item.keys()
            #     and not task_item["register"].startswith("__")
            #     and not task_item["register"].endswith("__")
            # ):
            #     register_name = task_item["register"]
            #     register_query = task[self.task_marker].get("register_query", None)
            #
            #     if register_query is not None:
            #         register_query_token = "::{}".format(register_query)
            #     else:
            #         register_query_token = ""
            #
            #     if "." in register_name:
            #         register_var_name, _ = register_name.split(".", 1)
            #         register_temp_name = "__temp_{}__".format(register_var_name)
            #         task_item["register"] = register_temp_name
            #
            #         set_fact_task = {
            #             "name": "[registering variable '{}' ]".format(register_name),
            #             "set_fact": {
            #                 "{}".format(
            #                     register_var_name
            #                 ): "{{{{ {} | register_var_filter('{}') }}}}".format(
            #                     register_temp_name, register_name
            #                 )
            #             },
            #         }
            #         register_task = {
            #             "name": "[freckles register variable: {}{}]".format(
            #                 register_var_name, register_query_token
            #             ),
            #             "debug": {"msg": "{{{{ {} }}}}".format(register_var_name)},
            #         }
            #         result.append(set_fact_task)
            #         result.append(register_task)
            #     else:
            #
            #         register_task = {
            #             "name": "[freckles register variable: {}{}]".format(
            #                 register_name, register_query_token
            #             ),
            #             "debug": {"msg": "{{{{ {} }}}}".format(register_name)},
            #         }
            #         result.append(register_task)

        return result

    def add_role_to_addition_files(self, command, path=None):

        if path is None:
            path = self.context.get_role_path(command)

        remote_role = path == command

        if not remote_role:
            if path not in self.additional_files:
                self.additional_files[path] = {
                    "type": ADD_TYPE_ROLE,
                    "target_name": command,
                }
        else:
            if command not in self.external_roles:
                self.external_roles.add(command)

    def add_tasklist_to_additional_files(self, tasklist_name, tasklist_var):

        if tasklist_var in self.additional_files.keys():
            return

        tasklist = self.context.get_tasklist(tasklist_name)

        self.additional_files[tasklist_var] = {
            "type": ADD_TYPE_TASK_LIST,
            "target_name": tasklist_var,
            "var_name": tasklist_var,
            "tasklist": tasklist,
        }
