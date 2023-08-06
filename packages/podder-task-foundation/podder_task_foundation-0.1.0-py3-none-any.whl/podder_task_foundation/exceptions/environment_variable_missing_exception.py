from .podder_task_exception import PodderTaskException


class EnvironmentVariableMissingException(PodderTaskException):
    default_how_to_solve = ''
    default_reference_url = 'https://podder.ai/'

    def __init__(self,
                 environment_variable_name: str,
                 detail: str,
                 how_to_solve: str = '',
                 reference_url: str = ''):
        message = "Environment " + environment_variable_name + ' is not set.'
        self.message = message
        self.detail = detail
        self.how_to_solve = how_to_solve or self.default_how_to_solve
        self.reference_url = reference_url or self.default_reference_url
        Exception.__init__(self, self.message, self.how_to_solve, self.default_reference_url)
