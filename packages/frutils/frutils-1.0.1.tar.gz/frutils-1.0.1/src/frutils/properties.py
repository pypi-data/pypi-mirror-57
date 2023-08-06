# -*- coding: utf-8 -*-
import copy
from collections import Sequence, Mapping

import dpath
from six import string_types

from frutils.doc import Doc


class Prop(object):
    @classmethod
    def from_dict(cls, data, parent_key=None):

        data = copy.deepcopy(data)
        doc = data.pop("doc", None)
        cli = data.pop("cli", None)
        alias = data.pop("alias", None)
        if alias is None:
            if parent_key is None:
                raise ValueError(
                    "Can't assemble Prop object: No 'alias' key in property dictionary, and not parent_key provided."
                )
            alias = parent_key

        meta = {}
        if cli:
            meta["cli"] = cli
        if parent_key:
            meta["parent_key"] = parent_key
        return Prop(alias=alias, schema=data, doc=doc, meta={"cli": cli})

    def __init__(self, alias, schema=None, doc=None, meta=None):

        self._alias = alias
        if schema is None:
            schema = {}
        self._schema = schema
        if doc is None:
            doc = {}
        self._doc = Doc(doc)
        if meta is None:
            meta = {}
        self._meta = meta

    @property
    def alias(self):
        return self._alias

    @property
    def schema(self):
        return self._schema

    @property
    def doc(self):
        return self._doc

    @property
    def meta(self):
        return self._meta


class PropSchemaItem(object):
    def __init__(self, prop, path):

        self._prop = prop
        self._path = path

    @property
    def prop(self):
        return self._prop

    @property
    def path(self):
        return self._path

    def __repr__(self):

        return "[Item: name='{}', path='{}']".format(self.prop.alias, self.path)


def find_property_schema_items(
    data, marker="__prop__", current=None, current_path=None
):

    if current is None:
        current = []
    if current_path is None:
        current_path = []

    if isinstance(data, string_types):
        return current
    elif isinstance(data, Sequence):
        for d in data:
            find_property_schema_items(
                d, marker=marker, current=current, current_path=current_path
            )
        return current
    elif isinstance(data, Mapping):
        if not current_path:
            key = "__root__"
        else:
            key = current_path[-1]
        for k, v in data.items():
            if k != marker:
                current_path_temp = copy.copy(current_path)
                current_path_temp.append(k)
                find_property_schema_items(
                    v, marker=marker, current=current, current_path=current_path_temp
                )
            else:
                if not isinstance(v, Mapping):
                    raise TypeError(
                        "Value of key with marker '{}' must be a mapping: {}".format(
                            marker, v
                        )
                    )
                prop = Prop.from_dict(parent_key=key, data=v)
                prop_item = PropSchemaItem(prop=prop, path=".".join(current_path))
                current.append(prop_item)
        return current


class PropSchema(object):
    @classmethod
    def parse_data(cls, data, marker="__prop__"):

        prop_items = find_property_schema_items(data, marker=marker)
        prop_schema = PropSchema(prop_schema_items=prop_items)
        return prop_schema

    def __init__(self, prop_schema_items=None):

        if prop_schema_items is None:
            prop_schema_items = []
        if isinstance(prop_schema_items, PropSchemaItem):
            prop_schema_items = [prop_schema_items]
        if not isinstance(prop_schema_items, Sequence):
            raise TypeError(
                "Can't create PropertySchema, invalid init type: {}".format(
                    type(prop_schema_items)
                )
            )

        self._items = {}
        self._item_list = []
        for item in prop_schema_items:
            self.add_item(item)
            self._item_list.append(item)

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        if not isinstance(item, PropSchemaItem):
            raise TypeError("Not a property schema item: {}".format(item))

        if not item.path:
            if self._items:
                raise ValueError(
                    "PropertySchema can't contain item with empty path as well as other items."
                )
            self._items["__root__"] = item
            return
        else:
            if self._items.get("__root__", None):
                raise ValueError(
                    "PropertySchema can't contain item with empty path as well as other items."
                )

        try:
            dpath.util.get(self._items, item.path, separator=".")
            raise ValueError(
                "Can't add schema item, path exists already: {}".format(item.path)
            )
        except (KeyError):
            # that's what we want
            pass

        dpath.util.new(self._items, item.path, item, separator=".")

    @property
    def item_list(self):
        return self._item_list

    def __repr__(self):
        all_paths = [x.path for x in self.item_list]
        return "[PropSchema: paths='{}'".format(",".join(all_paths))
