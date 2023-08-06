import uuid
from typing import Optional

from .config import Config
from .file import File
from .log.loggers import BaseLogger, ServerLogger, TaskLogger


class Context(object):
    @property
    def config(self) -> Config:
        return self._config

    @property
    def file(self) -> File:
        return self._file

    @property
    def mode(self) -> str:
        return self._mode

    @property
    def logger(self) -> BaseLogger:
        return self._logger

    @property
    def dag_id(self) -> str:
        return self._dag_id

    def __init__(self, mode: str, dag_id: Optional[str] = None,
                 config_path: Optional[str] = None) -> None:
        self._mode = mode
        self._dag_id = dag_id
        self._config = Config(self._mode, config_path)
        self._file = File(self._config)
        self._logger = self._get_logger()

    def _get_logger(self) -> BaseLogger:
        if self._dag_id is None:
            return ServerLogger(self.mode, self._config, str(uuid.uuid1()))

        return TaskLogger(self.mode, self._config, self._dag_id)
