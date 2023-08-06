from pathlib import Path

from .podder_task_exception import PodderTaskException


class DirectoryNotFoundException(PodderTaskException):
    default_how_to_solve = ''
    default_reference_url = 'https://podder.ai/'

    def __init__(self, path: Path, detail: str, how_to_solve: str, reference_url: str):
        message = "Directory " + str(path.resolve()) + ' does not exist.'
        self.message = message
        self.detail = detail
        self.how_to_solve = how_to_solve or self.default_how_to_solve
        self.reference_url = reference_url or self.default_reference_url
        Exception.__init__(self, self.message, self.how_to_solve, self.default_reference_url)
