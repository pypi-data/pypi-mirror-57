# -*- coding: utf-8 -*-
import copy
import hashlib
import inspect
import os
import re
from collections import Sequence

from inflection import camelize
from jinja2 import contextfilter
from markupsafe import Markup
from passlib.handlers.sha2_crypt import sha512_crypt
from passlib.hash import postgres_md5
from six import string_types
from slugify import slugify

from .doc import Doc
from .frutils import DEFAULT_ENV, dict_merge, readable_yaml, StringYAML


# def top_level_functions(body):
#     return (f for f in body if isinstance(f, ast.FunctionDef))
#
# def parse_ast(filename):
#     with open(filename, "rt") as file:
#         return ast.parse(file.read(), filename=filename)
#


def to_yaml_filter(value, readable=False, indent=0):
    """Returns a yaml string of the provided object/dict.

    Args:
      value (object): the input object/dict
      readable: whether to output a readable multiline string
      indent: whether and how much to indent the result

    Returns:
      string: a yaml-formatted string
    """

    if not value:
        return ""

    if not readable:
        yaml = StringYAML()
        yaml.default_flow_style = True
        result = yaml.dump(value)
        result = result.strip()
    else:
        result = readable_yaml(value, indent=indent)

    return result


def negate_filter(value):
    """
    Negates a boolean value.

    If the input is not a boolean, it will be converted to one: bool(value)

    Args:
      value (bool, object): the input
    Returns:
      bool: the inverse
    """

    if not isinstance(value, bool):
        value = bool(value)

    return not value


def negate_or_default_filter(value, default):
    """
    Negates a value if it is a bool, otherwise returns the default value.

    This is useful for example to pipe in potential None values or empty strings, and get back a default value if that is the case.

    Args:
      value (bool): the value
      default (bool): the default if value is not a bool
    Returns:
      bool: the default
    """

    if isinstance(value, bool):
        return negate_filter(value)

    if not isinstance(default, bool):
        raise Exception("negate default needs to be of type bool: {}".format(default))
    return default


def camelize_filter(value, replace_dashes=False):
    """
    Returns the input string, converted to CamelCase.

    Returns an empty string if no value was provided.

    Args:
        value (string): the original string
        remove_dashes (bool): whether to replace dashes with underscores before camelizing
    Returns:
        string: the camel-cased string
    """

    if not value:
        return ""

    if replace_dashes:
        value = value.replace("-", "_")

    return camelize(value)


def quote_filter(value, single_quotes=False):
    """
    Wraps an input string in quotes.

    Args:
        value (string): the original string
    Returns:
        string: the quoted string
    """

    if single_quotes:
        return "'" + str(value) + "'"
    else:
        return '"' + str(value) + '"'


def default_if_empty_filter(value, default):
    """
    Returns a default if provided with an empty value.

    Test for empty is: 'not value'. If value is a bool, it will be returned as is.

    Args:
      value (object): the input
      default (object): the default
    Returns:
      object: the value itself, or the default if empty
    """

    if isinstance(value, bool):
        return value

    if not value:
        return default
    else:
        return value


def string_for_boolean_filter(value, true_value, false_value):
    """
    Returns a different object depending on whether the value resolves to True or not.

    Test for True is simply: 'if value'.

    Args:
      value (object): the input
      true_value (object): the result if input is True
      false_value (object): the result if input is False
    Result:
      object: the result
    """

    if value:
        return true_value
    else:
        return false_value


def true_if_not_empty_filter(value):
    """
    Returns true if the value is not empty.

    This is the same as the 'false_if_empty'-filter.

    Args:
      value (object): the input
    Result:
      bool:
    """

    return false_if_empty_filter(value)


# def true_if_all_not_empty_filter(*value):
#
#     for v in value:
#         if not isinstance(v, bool) and not v:
#             return False
#
#     return True


def true_if_all_empty_filter(*value):
    """
    Returns true if all values are empty.

    Boolean 'False' doesn't count as empty.
    """

    for v in value:
        if isinstance(v, bool) or v:
            return False

    return True


def true_if_all_true_filter(*value):
    """
    Returns true if all values have a 'true-ish' value.

    Args:
        *value: list of values

    Returns: 'true' if all values have a 'true-ish' value
    """

    for v in value:
        if not v:
            return False

    return True


def true_if_all_false_filter(*value):
    """
    Returns true if all values have a non-'true-ish' value.

    Args:
        *value: list of values

    Returns: 'true' if all values have a non-'true-ish' value
    """

    for v in value:
        if v:
            return False

    return True


def false_if_all_true_filter(*value):
    """
    Returns false if all values have a 'true-ish' value.

    Args:
        *value: list of values

    Returns: 'true' if all values have a 'true-ish' value
    """

    for v in value:
        if not v:
            return True

    return False


def false_if_all_false_filter(*value):
    """
    Returns false if all values have a non-'true-ish' value.

    Args:
        *value: list of values

    Returns: 'false' if all values have a non-'true-ish' value
    """

    for v in value:
        if v:
            return True

    return False


def false_if_not_empty_filter(value):
    """
    Returns 'false' if the provided value is not empty.

    Args:
      value (object): the value
    Result:
      boolean: the result
    """

    if isinstance(value, bool) or value:
        return False
    else:
        return True


def false_if_all_not_empty_filter(*value):
    """
    Returns false if all provided values are non-empty.

    Args:
      value (list): a list of inputs
    Result:
      bool: true if at least one provided value is empty, false if all are non-empty, or the list is empty
    """

    for v in value:
        if not isinstance(v, bool) and not v:
            return True

    return False


def false_if_all_empty_filter(*value):
    """
    Returns false if all provided values are empty.

    Args:
      value (list): a list of inputs
    Result:
      bool: true if at least one provided value is non-empty, false if all are empty, or the list is empty.
    """

    for v in value:
        if isinstance(v, bool) or v:
            return True

    return False


def true_if_empty_filter(value):
    """
    Returns 'true' if the provided value is empty.

    Args:
      value (object): the value
    Result:
      boolean: the result
    """

    if not isinstance(value, bool) and not value:
        return True
    else:
        return False


def true_if_empty_or_filter(value, *or_values):
    """
    Returns 'true' if the provided value is empty or matches any of the provided values.

    Args:
      value (object): the value
      or_values (list): or_values
    Result:
      boolean: the result
    """

    if not isinstance(value, bool) and not value:
        return True
    else:
        if value in or_values:
            return True
        else:
            return False


def false_if_empty_filter(value):
    """
    Returns 'false' if the provided value is empty.

    Args:
      value (object): the value
    Result:
      boolean: the result
    """

    if not isinstance(value, bool) and not value:
        return False
    else:
        return True


def true_if_equal_filter(*value):
    """
    Returns 'true' if all values are equal, otherwise 'false'.
    """

    first = True
    eq = None
    for v in value:
        if first:
            eq = v
            first = False
            continue
        if eq != v:
            return False

    return True


def false_if_equal_filter(*value):
    """
    Returns 'false' if all values are equal, otherwise 'true'.
    """

    first = True
    eq = None
    for v in value:
        if first:
            eq = v
            first = False
            continue
        if eq != v:
            return True

    return False


def none_if_empty_filter(value):
    """
    Returns None value if input is an empty value.
    Args:
        value: the value

    Returns: None if the value is empty, otherwise the value

    """

    if isinstance(value, string_types):
        value = value.strip()

    if not value:
        return None
    else:
        return value


def basename_filter(path):
    """
    Returns the basename (without trailing slash) of a path.

    Args:
      path (str): the path to a folder or file
    Result:
      str: the basename
    """
    if path.endswith(os.path.sep):
        path = path[:-1]
    return os.path.basename(path)


def dirname_filter(path):
    """
    Returns the dirname (without trailing slash) of a path.

    Args:
      path (str): the path to a folder or file
    Result:
      str: the dirname
    """

    if not path:
        return None

    if path.endswith(os.path.sep):
        path = path[:-1]
    return os.path.dirname(path)


def clean_string_filter(string):
    """
    Returns a string with all non char/digit characters replaced with '_'.
    """
    if isinstance(string, string_types):
        result = re.sub("[^A-Za-z0-9]+", "_", string)
    else:
        result = string

    return result


def none_if_equals_filter(value, equal):
    """
    Returns 'None' if the input equals the other value, otherwise it returns the input.

    Args:
        value: the input value
        equal: the other value
    Result:
        obj, None: the result
    """

    if value == equal:
        return None
    else:
        return value


def sha512_crypt_filter(value, rounds=5000):
    """
    Returns an sha512-encrypted hash of the provided input.

    Args:
        value (str): the input
        rounds (int): how many rounds to use for hashing (default: 5000)

    Returns:
        str: the hash
    """

    if not value:
        return None

    hashed_pass = sha512_crypt.using(rounds=rounds).hash(value)
    return hashed_pass


def md5sum_filter(input):
    """
    Returns the md5 sum of a string.
    """

    input = input.encode("utf-8")
    result = hashlib.md5(input).hexdigest()
    return result


def postgresql_password_hash_filter(password, username):
    """Returns an encoded string that PostgreSQL accepts as an 'encrypted' password.

    If either the password or username are empty, 'None' will be returned.

    Args:
        password (str): the password
        username (str): the username
    """

    if not password or not username:
        return None

    result = postgres_md5.hash(password, user=username)

    return result


def slugify_filter(input, valid_var_name=False):
    """
    Returns a slugified version of the provided input.
    Args:
        input (str): the input string
        valid_var_name (bool): whether the result should be a valid Python var name (default: False)

    Returns:
        str: the slugified string

    """

    if not input:
        return input

    result = slugify(input)

    if valid_var_name:
        result = result.replace("-", "_")
        result = result.replace(".", "_")

    return result


def and_item_filter(a_list, input):

    if isinstance(a_list, string_types):
        a_list = [a_list]
    if not isinstance(a_list, Sequence):
        a_list = [a_list]

    result = a_list + [input]
    return result


def and_items_filter(a_list, *additional_items):

    if isinstance(a_list, string_types):
        a_list = [a_list]
    if not isinstance(a_list, Sequence):
        a_list = [a_list]

    result = copy.copy(a_list)

    for input in additional_items:
        if isinstance(input, string_types):
            input = [input]
        if not isinstance(input, Sequence):
            input = [input]

        result = result + input

    return result


def contains_filter(value, item):
    """
    Checks whether the provided value contains the item.

    Internally, this uses the Python 'in' check.

    Args:
        value: the value
        item: the contained item

    Returns: True if the item is found in the value

    """

    return item in value


def frecklet_name_filter(value):
    """
    Extracts the name of a frecklet from a path string.

    If value does not end with '.frecklet', the full filename will be returned.

    Args:
        value: the path or file name

    Returns: the frecklet name
    """

    result = os.path.basename(value)

    if result.endswith(".frecklet"):
        result = os.path.splitext(result)[0]

    return result


def split_string_filter(value, separator=os.path.sep, index=None):
    """
    Splits a string using the provided separator.

    Args:
        value: the value
        separator: the separator
        index: optional index, if provided, the 'index'-ed item will be returned, otherwise the whole list

    """
    token_list = value.split(separator)

    if index is not None:
        return token_list[index]
    else:
        return token_list


def first_non_empty_filter(*values, default=None):
    """
    Returns the first non-empty (non-None or non-empty String/List/Dict/etc.).

    If value is a boolean or integer, it'll return it, even if the value is False/0.

    Args:
        *values: A list of values
        default: default value, if no non_empty value is found

    Returns:
        The first non-empty element, None if no non-empty element is found.
    """

    for v in values:

        if isinstance(v, bool) or v:
            return v

    return default


# from: https://stackoverflow.com/questions/8862731/jinja-nested-rendering-on-variable-content
@contextfilter
def subrender_filter(context, value):
    _template = context.eval_ctx.environment.from_string(value)
    result = _template.render(**context)

    if context.eval_ctx.autoescape:
        result = Markup(result)
    return result


ALL_MEMBERS = locals()


def get_all_filter_functions():

    result = {}

    for func_name, func in ALL_MEMBERS.items():
        if not func_name.endswith("filter"):
            continue

        help = func.__doc__
        if not help:
            help = "n/a"
        help = inspect.cleandoc(help)

        doc = Doc({"help": help})
        name = func_name[0:-7]

        result[name] = {"func": func, "doc": doc}

    return result


ALL_FRUTIL_FILTERS = get_all_filter_functions()


def get_jinja_default_filters():

    result = {}

    for filter_name, func in DEFAULT_ENV.filters.items():

        help = func.__doc__
        help = inspect.cleandoc(help)
        doc = Doc({"help": help})

        result[filter_name] = {"func": func, "doc": doc}

    return result


ALL_DEFAULT_JINJA2_FILTERS = get_jinja_default_filters()

ALL_FILTERS = dict_merge(ALL_DEFAULT_JINJA2_FILTERS, ALL_FRUTIL_FILTERS, copy_dct=True)
