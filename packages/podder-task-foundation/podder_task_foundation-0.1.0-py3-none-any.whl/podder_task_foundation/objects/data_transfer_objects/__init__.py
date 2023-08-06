from .dataset import Dataset
from .images import Images

__all__ = ['Dataset', 'get_data_transfer_object']

_TYPES = {
    "dataset": Dataset,
    "images": Images,
}


def get_data_transfer_object(type_: str):
    if type_ in _TYPES:
        return _TYPES[type_]

    return Dataset
