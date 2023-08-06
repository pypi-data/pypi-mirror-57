from collections import OrderedDict
from typing import Any, Dict, List, Optional

from podder_task_foundation.exceptions import AmbiguousParameterException
from podder_task_foundation.objects.data import File

from ..data import Data
from ..object import Object


class Dataset(Object):

    _properties = OrderedDict({
        'dataset': [],
        'properties': {},
    })

    @staticmethod
    def get_type():
        return 'dataset'

    def __init__(self, dict_: Optional[Dict] = None):
        self._type = self.get_type()
        super().__init__(dict_=dict_)

    def add_data(self, data: Any):
        if not isinstance(data, dict):
            raise AmbiguousParameterException(
                "Wrong data structure", "Data which you add has wrong structure and cannot add",
                "Currently datasets requires dict with path and name", "https://podder.ai/")

        if 'path' not in data:
            raise AmbiguousParameterException(
                "Wrong data structure", "Data which you add has wrong structure and cannot add",
                "Currently datasets requires dict with path and name", "https://podder.ai/")

        name = None
        if 'name' in data:
            name = data["name"]

        return self.add_file(name=name, path=data["path"])

    def add_file(self, path: str, name: Optional[str] = None):
        if name is None:
            name = "file"
        file = File(name=name, path=path)
        self._dict['dataset'].append(file)

    def get_file(self, name: Optional[str] = None):
        if name is None:
            if len(self._dict['dataset']) == 1:
                return self._dict['dataset'][0].path
            else:
                candidates = ",".join([dataset.name for dataset in self._dict['dataset']])
                raise AmbiguousParameterException(
                    "Name should be specified",
                    "This dataset includes multiple files. Need to specify name to get file",
                    "Currently this dataset have the following names: " + candidates,
                    "https://podder.ai/")

        for dataset in self._dict['dataset']:
            if dataset.name == name:
                return dataset.path

        return None

    def add_error(self,
                  code: str,
                  message: str,
                  object_id: Optional[str] = None,
                  name: Optional[str] = None):
        if name is None:
            name = "file"
        file = File(name=name, path="")
        file.add_error(code, message)
        self._dict['dataset'].append(file)

    def get_all_files(self):
        return [dataset.path for dataset in self._dict['dataset']]

    def get_all_data(self) -> List[Data]:
        return self._dict['dataset']

    def set_property(self, key: str, value: Any):
        self._dict['properties'][key] = value

    def get_property(self, key: str, default: Any = None):
        if key in self._dict['properties']:
            return self._dict['properties'][key]
        return default

    @property
    def type(self) -> str:
        return self._type
