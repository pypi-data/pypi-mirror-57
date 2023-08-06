import configparser
from pathlib import Path

from podder_task_foundation.config.parsers.base import BaseConfigParser


class IniConfigParser(BaseConfigParser):
    @classmethod
    def name(cls) -> str:
        return "json"

    @classmethod
    def detect_target(cls, file: Path) -> bool:
        if file.suffix.lower() == 'json':
            return True

        return False

    @classmethod
    def parse(cls, file) -> dict:
        parser = configparser.ConfigParser()
        data = parser.read_string(file.read_text())
        result = data.defaults()
        for section in data.sections():
            result[section] = {}
            for key in data[section]:
                result[section][key] = data[section][key]

        return result
