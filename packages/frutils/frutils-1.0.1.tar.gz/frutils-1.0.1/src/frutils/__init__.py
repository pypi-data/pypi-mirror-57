# -*- coding: utf-8 -*-
import importlib
import io
import os

from pkg_resources import DistributionNotFound, get_distribution

from .defaults import (
    DEFAULT_BLOCK_END_STRING,
    DEFAULT_BLOCK_START_STRING,
    DEFAULT_DOWNLOAD_CACHE_BASE,
    DEFAULT_EXCLUDE_DIRS,
    DEFAULT_LOCAL_ENV_VARS_KEY,
    DEFAULT_URL_ABBREVIATIONS_FILE,
    DEFAULT_URL_ABBREVIATIONS_REPO,
    DEFAULT_VARIABLE_END_STRING,
    DEFAULT_VARIABLE_START_STRING,
    JINJA_DELIMITER_PROFILES,
    KEY_ALIAS_NAME,
    KEY_ARGS_GROUP,
    KEY_ARGUMENT_TYPE,
    KEY_CLI_CLICK_ARGUMENT_NAME,
    KEY_CLI_CLICK_OPTIONS_NAME,
    KEY_CLI_CLICK_PARAM_NAME,
    KEY_CLI_GROUP,
    KEY_DEFAULT_VALUE_NAME,
    KEY_DOC_GROUP,
    KEY_EPILOG_NAME,
    KEY_HELP_NAME,
    KEY_INCLUDE_DEFAULT_VARS_NAME,
    KEY_META_GROUP,
    KEY_OPTION_TYPE,
    KEY_PARAM_ENABLED_NAME,
    KEY_PARAMETER_TYPE,
    KEY_REQUIRED_DEFAULT,
    KEY_REQUIRED_NAME,
    KEY_SHORT_HELP_NAME,
    KEY_TYPE_DEFAULT,
    KEY_TYPE_NAME,
    KEY_VARS_GROUP,
    SUPPORTED_OUTPUT_FORMATS,
    URL_PLACEHOLDER,
)

# <AUTOGEN_INIT>
from .frutils import (
    DEFAULT_ENV,
    IgnoreUndefinedJinjaVariable,
    StringYAML,
    add_key_to_dict,
    append_key_to_dict,
    auto_parse_string,
    calculate_cache_location_for_url,
    can_passwordless_sudo,
    dict_merge,
    ensure_git_repo_format,
    ensure_parent_dir,
    flatten_lists,
    get_git_auto_dest_name,
    get_key_path_value,
    get_template_keys,
    get_template_keys_from_string,
    get_terminal_size,
    is_list_of_strings,
    is_sequence,
    is_url_or_abbrev,
    list_of_special_dicts_to_list_of_dicts,
    log,
    merge_list_of_dicts,
    ordered_load,
    readable,
    readable_json,
    readable_pformat,
    readable_raw,
    readable_yaml,
    reindent,
    replace_string,
    replace_strings_in_obj,
    special_dict_to_dict,
    string_is_templated,
    unsorted_to_sorted_dict,
)

try:
    importlib.import_module("click")
    from .frutils_cli import output
except ImportError:
    pass

__author__ = """Markus Binsteiner"""
__email__ = "makkus@frkl.io"

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    try:
        version_file = os.path.join(os.path.dirname(__file__), "version.txt")

        if os.path.exists(version_file):
            with io.open(version_file, encoding="utf-8") as vf:
                __version__ = vf.read()
        else:
            __version__ = "unknown"

    except (Exception):
        pass

    if __version__ is None:
        __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound

# flake8: noqa

__submodules__ = ["frutils", "defaults"]


__all__ = [
    "DEFAULT_BLOCK_END_STRING",
    "DEFAULT_BLOCK_START_STRING",
    "DEFAULT_DOWNLOAD_CACHE_BASE",
    "DEFAULT_ENV",
    "DEFAULT_EXCLUDE_DIRS",
    "DEFAULT_LOCAL_ENV_VARS_KEY",
    "DEFAULT_URL_ABBREVIATIONS_FILE",
    "DEFAULT_URL_ABBREVIATIONS_REPO",
    "DEFAULT_VARIABLE_END_STRING",
    "DEFAULT_VARIABLE_START_STRING",
    "IgnoreUndefinedJinjaVariable",
    "JINJA_DELIMITER_PROFILES",
    "KEY_ALIAS_NAME",
    "KEY_ARGS_GROUP",
    "KEY_ARGUMENT_TYPE",
    "KEY_CLI_CLICK_ARGUMENT_NAME",
    "KEY_CLI_CLICK_OPTIONS_NAME",
    "KEY_CLI_CLICK_PARAM_NAME",
    "KEY_CLI_GROUP",
    "KEY_DEFAULT_VALUE_NAME",
    "KEY_DOC_GROUP",
    "KEY_EPILOG_NAME",
    "KEY_HELP_NAME",
    "KEY_INCLUDE_DEFAULT_VARS_NAME",
    "KEY_META_GROUP",
    "KEY_OPTION_TYPE",
    "KEY_PARAMETER_TYPE",
    "KEY_PARAM_ENABLED_NAME",
    "KEY_REQUIRED_DEFAULT",
    "KEY_REQUIRED_NAME",
    "KEY_SHORT_HELP_NAME",
    "KEY_TYPE_DEFAULT",
    "KEY_TYPE_NAME",
    "KEY_VARS_GROUP",
    "SUPPORTED_OUTPUT_FORMATS",
    "StringYAML",
    "URL_PLACEHOLDER",
    "add_key_to_dict",
    "append_key_to_dict",
    "calculate_cache_location_for_url",
    "can_passwordless_sudo",
    "defaults",
    "dict_merge",
    "ensure_git_repo_format",
    "ensure_parent_dir",
    "flatten_lists",
    "frutils",
    "get_git_auto_dest_name",
    "get_key_path_value",
    "get_template_keys",
    "get_template_keys_from_string",
    "is_list_of_strings",
    "is_sequence",
    "string_is_templated",
    "is_url_or_abbrev",
    "list_of_special_dicts_to_list_of_dicts",
    "log",
    "merge_list_of_dicts",
    "ordered_load",
    "readable",
    "readable_json",
    "readable_pformat",
    "readable_raw",
    "readable_yaml",
    "reindent",
    "replace_string",
    "replace_strings_in_obj",
    "special_dict_to_dict",
]
# </AUTOGEN_INIT>
