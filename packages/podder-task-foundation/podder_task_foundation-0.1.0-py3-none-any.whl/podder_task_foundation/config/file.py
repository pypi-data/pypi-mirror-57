from pathlib import Path
from typing import Optional

from podder_task_foundation.config.parsers import JsonConfigParser, YamlConfigParser

_all_parsers = [
    JsonConfigParser,
    YamlConfigParser,
]


class File(object):
    def __init__(self, file: Path):
        self._file = file

    def parse(self) -> Optional[dict]:
        data = {}

        for parser in _all_parsers:
            if not parser.detect_target(self._file):
                continue
            data = parser.parse(self._file)

        return data
