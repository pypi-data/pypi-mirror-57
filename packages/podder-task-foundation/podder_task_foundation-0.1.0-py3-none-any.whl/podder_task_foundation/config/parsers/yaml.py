from collections import OrderedDict
from pathlib import Path

import yaml
from podder_task_foundation.config.parsers.base import BaseConfigParser


def represent_odict(dumper, instance):
    return dumper.represent_mapping('tag:yaml.org,2002:map', instance.items())


yaml.add_representer(OrderedDict, represent_odict)


class YamlConfigParser(BaseConfigParser):
    @classmethod
    def name(cls) -> str:
        return "yaml"

    @classmethod
    def detect_target(cls, file: Path) -> bool:
        if file.suffix.lower() == '.yaml' or file.suffix.lower() == '.yml':
            return True

        return False

    @classmethod
    def parse(cls, file) -> dict:
        return yaml.load(file.read_text(), Loader=yaml.SafeLoader)
