import sys
import uuid
from pathlib import Path

from podder_task_foundation.objects.data_transfer_object_group import (
    INTERFACE,
    DataTransferObjectGroup,
)

from ..config import Config
from ..file import File


class ArgumentParser(object):
    def __init__(self, config: Config, file: File, job_id: str):
        self._config = config
        self._file = file
        self._job_id = job_id
        self._inputs = DataTransferObjectGroup(
            config=self._config, interface_type=INTERFACE.INPUT, job_id=str(uuid.uuid1()))
        self._parse_arguments()

    def _parse_arguments(self):
        keys = self._inputs.get_interface_keys()
        interfaces = {}
        for key in keys:
            interfaces[key] = self._inputs.get_interface(key)
        arguments = sys.argv[1:]
        for argument in arguments:
            if argument[0:2] == '--' and argument.find('=') >= 0:
                elements = argument[2:].split("=", 1)
                if elements[0] in keys:
                    interfaces[elements[0]].add_file(self._normalize_file_path(elements[1]))
            elif argument[0:1] == '-':
                pass
            else:
                if len(keys) == 1:
                    interfaces[keys[0]].add_file(self._normalize_file_path(argument))

    def _normalize_file_path(self, path):
        input_file = self._file.get_input_file(path)
        if input_file.exists():
            return str(input_file)
        current_directory_path = Path(input_file)
        if current_directory_path.exists():
            return str(current_directory_path.resolve())

        return path

    def get_input(self) -> DataTransferObjectGroup:
        return self._inputs
