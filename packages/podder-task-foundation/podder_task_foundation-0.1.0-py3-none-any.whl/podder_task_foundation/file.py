import os
from pathlib import Path

from .config import Config
from .exceptions import DirectoryNotFoundException, FileNotFoundException


class File(object):
    """
    File assessor
    All tasks need to access file through this class
    """

    def __init__(self, config: Config):
        self._config = config
        self._root_path = os.path.abspath(config.get('file.root_directory', './'))

    def get_root_path(self) -> str:
        return self._root_path

    def get_input_path(self, path: str = '') -> str:
        """
        Returns absolute path to `input` directory.
        """
        directory_path = self._config.get('file.input_directory',
                                          os.path.join(self.get_root_path(), 'input'))

        directory_path_object = Path(directory_path)
        if not Path(directory_path).exists():
            raise DirectoryNotFoundException(
                directory_path_object,
                detail="Input directory should be placed on " + str(
                    directory_path_object.resolve()),
                how_to_solve="Create config directory on " + str(directory_path_object.resolve()) +
                " or set proper path on config file",
                reference_url="")

        return os.path.abspath(os.path.join(directory_path, path))

    def get_output_path(self, path: str = '') -> str:
        """
        Returns absolute path to `output` directory.
        """
        directory_path = self._config.get('file.output_directory',
                                          os.path.join(self.get_root_path(), 'output'))

        directory_path_object = Path(directory_path)
        if not Path(directory_path).exists():
            raise DirectoryNotFoundException(
                directory_path_object,
                detail="Output directory should be placed on " + str(
                    directory_path_object.resolve()),
                how_to_solve="Create config directory on " + str(directory_path_object.resolve()) +
                " or set proper path on config file",
                reference_url="")

        return os.path.abspath(os.path.join(directory_path, path))

    def get_data_path(self, path: str = '') -> str:
        """
        Returns absolute path to `data` directory.
        """
        directory_path = self._config.get('file.data_directory',
                                          os.path.join(self.get_root_path(), 'data'))

        directory_path_object = Path(directory_path)
        if not Path(directory_path).exists():
            raise DirectoryNotFoundException(
                directory_path_object,
                detail="Data directory should be placed on " + str(directory_path_object.resolve()),
                how_to_solve="Create config directory on " + str(directory_path_object.resolve()) +
                " or set proper path on config file",
                reference_url="")

        return os.path.abspath(os.path.join(directory_path, path))

    def get_temporary_path(self, path: str = '') -> str:
        """
        Returns absolute path to `tmp` directory.
        """
        directory_path = self._config.get('file.temporary_directory',
                                          os.path.join(self.get_root_path(), 'tmp'))

        return os.path.abspath(os.path.join(directory_path, path))

    def get_input_file(self, name: str) -> Path:
        path = Path(self.get_input_path(name))
        return path

    def get_data_file(self, name: str) -> Path:
        path = Path(self.get_input_path(name))
        return path

    def get_output_file(self, name: str) -> Path:
        path = Path(self.get_output_path(name))
        return path

    def _read_bytes_from_path(self, path: Path, encoding: str = 'utf-8') -> bytes:
        if not path.exists():
            raise FileNotFoundException(
                path,
                detail="File " + str(path.resolve()) + " does not exists",
                how_to_solve="Check where you placed your file",
                reference_url="")

        return path.read_bytes()

    def _read_text_from_path(self, path: Path, encoding: str = 'utf-8') -> str:
        if not path.exists():
            raise FileNotFoundException(
                path,
                detail="File " + str(path.resolve()) + " does not exists",
                how_to_solve="Check where you placed your file",
                reference_url="")

        return path.read_text(encoding)

    def read_bytes_from_input_file(self, name: str, encoding: str = 'utf-8') -> bytes:
        path = self.get_input_file(name)
        return self._read_bytes_from_path(path)

    def read_text_from_input_file(self, name: str, encoding: str = 'utf-8') -> str:
        path = self.get_input_file(name)
        return self._read_text_from_path(path)

    def read_bytes_from_data_file(self, name: str, encoding: str = 'utf-8') -> bytes:
        path = self.get_data_file(name)
        return self._read_bytes_from_path(path)

    def read_text_from_data_file(self, name: str, encoding: str = 'utf-8') -> str:
        path = self.get_data_file(name)
        return self._read_text_from_path(path)

    def write_bytes_to_output_file(self, name: str, data: bytes):
        path = self.get_output_file(name)
        path.write_bytes(data)

    def write_text_to_output_file(self, name: str, data: str, encoding: str = 'utf-8'):
        path = self.get_output_file(name)
        path.write_text(data, encoding)
