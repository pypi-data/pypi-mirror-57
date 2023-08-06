import copy
import json
import re
from collections import OrderedDict
from typing import Any, Dict, Optional


class Object(object):
    _properties = OrderedDict({})

    def __init__(self, dict_: Optional[Dict] = None):
        self._dict = copy.deepcopy(self._properties)
        self._build_dict(dict_)

    def __repr__(self):
        return self.to_json()

    def __str__(self):
        return self.to_json()

    def __getitem__(self, item):
        return self._dict[item]

    def __getattr__(self, item):
        if item not in self._properties.keys():
            raise AttributeError("'{}' object has no attribute '{}'".format(
                type(self).__name__, item))
        return self._dict[item]

    def __contains__(self, item):
        return item in self._properties.keys()

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self) -> Dict:
        return self._to_json_structure(self._dict)

    def _to_json_structure(self, data: Any) -> Any:
        if isinstance(data, dict):
            result_dict = OrderedDict()
            for key in data.keys():
                json_key = self._snake_to_camel(key)
                result_dict[json_key] = self._to_json_structure(data[key])
            return result_dict
        elif isinstance(data, (list, set)):
            result_array = []
            for value in data:
                result_array.append(self._to_json_structure(value))
            return result_array
        elif hasattr(data, 'to_dict'):
            return data.to_dict()
        else:
            return data

    def _build_dict(self, dict_: Optional[Dict]):
        if not isinstance(dict_, dict):
            return
        for key in self._properties.keys():
            if key in dict_:
                snake_key = self._camel_to_snake(key)
                self._dict[snake_key] = dict_[key]

    @staticmethod
    def _snake_to_camel(source: str) -> str:
        return re.sub("_(.)", lambda x: x.group(1).upper(), source)

    @staticmethod
    def _camel_to_snake(source: str) -> str:
        return re.sub("([A-Z])", lambda x: "_" + x.group(1).lower(), source)
