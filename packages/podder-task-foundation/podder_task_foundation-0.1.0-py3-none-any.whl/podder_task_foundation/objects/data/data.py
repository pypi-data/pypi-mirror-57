import json
import mimetypes
import uuid
from collections import OrderedDict
from pathlib import Path
from typing import Any, Dict, Optional, Union

import filetype
from podder_task_foundation.objects.errors import Error

from ..object import Object


class Data(Object):
    _properties = OrderedDict({
        'name': '',
        'errors': [],
        'objectId': '',
        'data': None,
    })

    @staticmethod
    def get_type():
        return 'object'

    def __init__(self,
                 dict_: Optional[Dict] = None,
                 name: Optional[str] = None,
                 object_id: Optional[str] = None):

        mimetypes.init()
        self._type = self.get_type()
        if not isinstance(dict_, dict):
            dict_ = {}
        if name is not None:
            dict_['name'] = name
        if object_id is not None:
            dict_['objectId'] = object_id
        super().__init__(dict_=dict_)
        self._check_and_generate_object_id()

    def add_error(self, code: Union[str, int], message: str):
        self._dict['errors'].append(Error(code, message))

    @staticmethod
    def is_file() -> bool:
        return False

    def get_file_path(self) -> Optional[str]:
        return None

    def get_text(self) -> str:
        return json.dumps(self._dict['data'])

    def _check_and_generate_object_id(self):
        if self._dict['objectId'] == '':
            self._dict['objectId'] = str(uuid.uuid1())

    def has_error(self) -> bool:
        return len(self.__dict['errors']) > 0

    def get_error(self) -> str:
        if not self.has_error():
            return ""
        result = ""
        for error in self.__dict['errors']:
            if result != '':
                result = result + '\n'
            result = result + error.message

        return result

    @property
    def media_type(self) -> str:
        media_type = "application/octet-stream"
        if self.is_file:
            path = self.get_file_path()
            if path is None:
                return media_type
            file_path = Path(path)
            extension = file_path.suffix

            if extension in mimetypes.types_map:
                return mimetypes.types_map[extension]
            else:
                kind = filetype.guess(file_path)
                if kind is not None:
                    return kind.mime

        return media_type

    @property
    def size(self) -> int:
        if self.is_file:
            path = self.get_file_path()
            if path is None:
                return 0
            else:
                path = Path(path)
                if not path.exists():
                    return 0
                return path.stat().st_size

        data = self.get_text()

        return len(data)
