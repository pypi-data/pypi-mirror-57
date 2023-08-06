import time

from . import BaseLogger
from ..config import Config


class TaskLogger(BaseLogger):
    def __init__(self, mode: str, config: Config):
        super().__init__(mode, config)
        self.start_time = time.time()
