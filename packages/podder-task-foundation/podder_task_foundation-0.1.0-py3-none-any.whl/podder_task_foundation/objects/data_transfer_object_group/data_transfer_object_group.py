from collections import OrderedDict
from typing import Any, Dict, List, Optional

from ...config import Config
from ...exceptions import AmbiguousParameterException
from ..data_transfer_objects import Dataset, get_data_transfer_object
from ..errors import Error
from ..object import Object
from .interface_type import INTERFACE


class DataTransferObjectGroup(Object):
    _properties = OrderedDict({
        'jobId': '',
        'errors': [],
        'data': {},
    })

    def __init__(self,
                 config: Config,
                 interface_type: INTERFACE.INPUT,
                 job_id: Optional[str] = None,
                 dict_: Optional[Dict] = None):
        self._config: Config = config
        self._job_id: str = job_id
        self._interface_type: str = interface_type
        self._dict: Dict = {}
        self._interface: Dict = self._get_interface_config()
        dict_ = {}
        if job_id is not None:
            dict_ = {'jobId': job_id}
        super().__init__(dict_=dict_)

    def __getitem__(self, item) -> Any:
        return self._dict[item]

    def __contains__(self, item) -> bool:
        return item in self._interface.keys()

    def add_error(self, code: str, message: str):
        self._dict['errors'].append(Error(code=code, message=message))

    @property
    def errors(self) -> str:
        return self._dict['errors']

    def add_file(self, path: str, name: Optional[str] = None,
                 interface_key: Optional[str] = None) -> None:
        interface_key = self._get_interface_key(interface_key)
        if self._dict['data'][interface_key] is None:
            self._dict['data'][interface_key] = self._create_dataset(interface_key)
        self._dict['data'][interface_key].add_file(name=name, path=path)

    def get_file(self, name: Optional[str] = None,
                 interface_key: Optional[str] = None) -> Optional[str]:
        interface_key = self._get_interface_key(interface_key)
        if self._dict['data'][interface_key] is None:
            return None
        return self._dict['data'][interface_key].get_file(name)

    def get_interface(self, interface_key: Optional[str] = None) -> Dataset:
        interface_key = self._get_interface_key(interface_key)
        if self._dict['data'][interface_key] is None:
            self._dict['data'][interface_key] = self._create_dataset(interface_key)

        return self._dict['data'][interface_key]

    def get_interface_keys(self) -> List:
        return list(self._interface.keys())

    def set_dataset(self, interface_key: Optional[str] = None,
                    dataset: Optional[Dataset] = None) -> None:
        interface_key = self._get_interface_key(interface_key)
        self._dict['data'][interface_key] = dataset

    def _get_interface_config(self) -> Dict:
        key = 'input'
        if self._interface_type == INTERFACE.OUTPUT:
            key = 'output'
        interfaces = self._config.get("app.interface." + key)
        if interfaces is None or type(interfaces) != dict:
            interfaces = OrderedDict({'interface': 'dataset'})
        return interfaces

    def _build_dict(self, dict_: Dict) -> None:
        keys = self.get_interface_keys()
        for key in keys:
            self._dict[key] = None
        if isinstance(dict_, dict):
            for key in keys:
                if key in dict_:
                    self._dict[key] = dict_[key]

        for key in self._interface.keys():
            self._dict['data'][key] = self._create_dataset(key)

    def _get_interface_key(self, interface_key: Optional[str] = None) -> str:
        keys = list(self._interface.keys())
        if interface_key is not None:
            if interface_key not in keys:
                candidates = ",".join(keys)
                raise AmbiguousParameterException(
                    "Specified interface key is not defined in this task",
                    "\"interface_key\" is not specified in the interface config",
                    "Currently this task have the following interfaces: " + candidates,
                    "https://podder.ai/")
        else:
            if len(keys) != 1:
                candidates = ",".join(keys)
                raise AmbiguousParameterException(
                    "Name should be specified", "This task has multiple interfaces for " +
                    self._interface_type + ". Need to specify name to access dataset",
                    "Currently this task have the following interface: " + candidates,
                    "https://podder.ai/")
            interface_key = keys[0]

        return interface_key

    def _create_dataset(self, interface_key: str) -> Dataset:
        dataset_type = self._interface[interface_key]
        dataset = (get_data_transfer_object(dataset_type))()
        return dataset

    @property
    def job_id(self) -> str:
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
