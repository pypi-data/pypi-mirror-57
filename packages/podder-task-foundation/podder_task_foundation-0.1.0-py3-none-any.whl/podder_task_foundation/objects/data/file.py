from collections import OrderedDict
from pathlib import Path
from typing import Any, Dict, Optional

from .data import Data


class File(Data):
    _properties = OrderedDict({
        'name': '',
        'path': '',
        'errors': [],
        'objectId': '',
    })

    @staticmethod
    def get_type():
        return 'file'

    def __init__(self,
                 dict_: Optional[Dict] = None,
                 name: Optional[str] = None,
                 path: Optional[str] = None,
                 object_id: Optional[str] = None):
        if not isinstance(dict_, dict):
            dict_ = {}
        if path is not None:
            dict_['path'] = path
        super().__init__(dict_=dict_, name=name, object_id=object_id)

    def _build_dict(self, dict_: Optional[Dict]):
        super()._build_dict(dict_)
        if not isinstance(dict_, dict):
            return
        if self._dict['name'] is None or self._dict['name'] == '':
            path_object = Path(self._dict['path'])
            self._dict['name'] = path_object.name

    def exists(self):
        path = Path(self._dict['path'])
        return path.exists()

    @staticmethod
    def is_file() -> bool:
        return True

    def get_file_path(self) -> Optional[str]:
        return self._dict['path']

    def get_text(self) -> str:
        path = Path(self._dict['path'])
        if not path.exists() or path.is_dir():
            return ""

        return path.read_text(encoding="utf-8")
