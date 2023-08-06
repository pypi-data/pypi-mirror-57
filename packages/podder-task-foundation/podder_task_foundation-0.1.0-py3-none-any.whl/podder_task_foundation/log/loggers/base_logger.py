import logging
import os
import sys
from typing import Dict, Optional

from colorlog import ColoredFormatter
from podder_task_foundation.config import Config
from podder_task_foundation.log.log_setting import LogSetting
from podder_task_foundation.mode import MODE


class BaseLogger(object):
    TRACE_LOG_LEVEL = 5

    def __init__(self, mode: str, config: Config, dag_id: str):
        self._mode = mode
        self._dagId = dag_id
        self._config = config
        self._add_trace_level()
        self._logger = self._get_logger()
        self.setting = LogSetting(mode, config).load()

    def _get_logger(self) -> Optional[logging.Logger]:
        if self._mode == MODE.CONSOLE:
            logger = logging.getLogger("console")
            return logger
        if self._mode == MODE.PIPELINE:
            logger = logging.getLogger("pipeline")
            return logger

        return None

    def trace(self, msg, *args, **kwargs):
        self._format(self.TRACE_LOG_LEVEL, msg, extra=self._create_extra(), *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self._format(logging.DEBUG, msg, extra=self._create_extra(), *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self._format(logging.INFO, msg, extra=self._create_extra(), *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self._format(logging.WARNING, msg, extra=self._create_extra(), *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        self._format(logging.WARNING, msg, extra=self._create_extra(), *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._format(logging.ERROR, msg, extra=self._create_extra(), *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        self._format(logging.ERROR, msg, extra=self._create_extra(), *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self._format(logging.CRITICAL, msg, extra=self._create_extra(), *args, **kwargs)

    @staticmethod
    def _convert_newline_character(msg: str) -> str:
        old_character = '\n'
        new_character = '\\n'

        return msg.replace(old_character, new_character)

    def _add_trace_level(self):
        logging.addLevelName(self.TRACE_LOG_LEVEL, "TRACE")

    def _format(self, level, msg, extra=None, *args, **kwargs):
        if self._logger is None:
            return
        self._logger.log(level, self._convert_newline_character(msg), extra=extra, *args, **kwargs)

    def _create_extra(self) -> Dict:
        return {}

    def _configure_logger(self, log_format: str, log_level):
        self._logger.setLevel(log_level)
        self._logger.propagate = False
        self._add_handler(log_format, log_level)

    def _add_handler(self, log_format: str, log_level):
        handler = self._default_handler()
        handler.setLevel(log_level)
        formatter = logging.Formatter(fmt=log_format, datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        if (self._logger.hasHandlers()):
            self._logger.handlers.clear()
        self._logger.addHandler(handler)

    def _default_handler(self):
        handler = logging.StreamHandler(sys.stdout)
        if self._support_color():
            color_formatter = self._get_color_formatter()
            handler.setFormatter(color_formatter)
        return handler

    def _get_color_formatter(self) -> ColoredFormatter:
        color_formatter = ColoredFormatter(
            log_colors=self.setting["log_colors"],
            secondary_log_colors=self.setting["secondary_log_colors"])
        return color_formatter

    @staticmethod
    def _support_color() -> bool:
        platform = sys.platform
        supported_platform = \
            platform != 'Pocket PC' and (platform != 'win32' or 'ANSICON' in os.environ)
        if not supported_platform:
            return False

        for handle in [sys.stdout, sys.stderr]:
            is_a_tty = hasattr(handle, 'isatty') and handle.isatty()
            if not is_a_tty:
                return False
        return True
