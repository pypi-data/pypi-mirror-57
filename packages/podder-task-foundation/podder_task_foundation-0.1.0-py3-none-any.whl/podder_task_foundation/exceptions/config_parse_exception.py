from pathlib import Path

from .podder_task_exception import PodderTaskException


class ConfigParseException(PodderTaskException):
    default_how_to_solve = ''
    default_reference_url = 'https://podder.ai/'

    def __init__(self, path: Path, parser_type: str, detail, how_to_solve: str, reference_url: str):
        message = "Parse config file " + str(
            path.resolve()) + ' failed with parser type ' + parser_type
        self.message = message
        self.detail = detail
        self.how_to_solve = how_to_solve or self.default_how_to_solve
        self.reference_url = reference_url or self.default_reference_url
        Exception.__init__(self, self.message, self.detail, self.how_to_solve,
                           self.default_reference_url)
