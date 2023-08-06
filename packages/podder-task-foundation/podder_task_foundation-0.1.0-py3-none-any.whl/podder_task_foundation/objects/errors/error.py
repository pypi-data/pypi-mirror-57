from collections import OrderedDict
from typing import Dict, Union

from ..object import Object


class Error(Object):
    _properties = OrderedDict({
        'code': '',
        'message': '',
    })

    def __init__(self, code: Union[str, int], message: str):
        dict_ = {
            'code': str(code),
            'message': message,
        }
        super().__init__(dict_=dict_)
