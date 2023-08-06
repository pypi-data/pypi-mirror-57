from podder_task_foundation.config import Config

from .base_logger import BaseLogger


class ServerLogger(BaseLogger):
    def __init__(self, mode: str, config: Config, dag_id: str):
        super().__init__(mode, config, dag_id)
        log_format = self.setting["default_log_format"]
        log_level = self.setting["server_log_level"]
        self._configure_logger(log_format, log_level)
