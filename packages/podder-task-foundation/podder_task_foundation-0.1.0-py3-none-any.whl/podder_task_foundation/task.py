import os
import sys
import traceback
from typing import Any, Optional

from podder_task_foundation.objects.data_transfer_object_group import (
    INTERFACE,
    DataTransferObjectGroup,
)

from .context import Context
from .exceptions import PodderTaskException
from .log.stream_to_logger import StreamToLogger
from .mode import MODE
from .utils import ArgumentParser


class Task(object):
    def __init__(self, mode: str, context: Optional[Context] = None) -> None:
        if context is None:
            context = Context(mode)
        self.context = context
        self.initialize(context)

    def initialize(self, context: Context) -> None:
        pass

    def execute_file(self, file_path: str, context: Context) -> Any:
        pass

    def handle(self, job_id: str, dag_id: str,
               input_: Optional[DataTransferObjectGroup] = None) -> DataTransferObjectGroup:

        outputs = DataTransferObjectGroup(
            config=self.context.config, interface_type=INTERFACE.OUTPUT, job_id=job_id)
        try:
            context = Context(self.context.mode, dag_id)
        except PodderTaskException as exception:
            self.context.logger.critical(exception.message)
            return outputs

        logger = context.logger
        sys.stdout = StreamToLogger(logger)

        try:
            if input_ is None:
                input_ = self._generate_input_data(context, job_id)

            return self.execute(input_, outputs, context)
        except PodderTaskException as exception:
            context.logger.critical(exception.message)
        except SystemExit as exception:
            context.logger.critical("system exit")
            outputs.add_error(code="NONE", message="system exit")
        except KeyboardInterrupt as exception:
            raise exception
        except Exception as exception:
            outputs.add_error(code="NONE", message=str(exception))

        return outputs

    def execute(self, inputs: DataTransferObjectGroup, outputs: DataTransferObjectGroup,
                context: Context) -> DataTransferObjectGroup:

        keys = inputs.get_interface_keys()
        if len(keys) > 1:
            PodderTaskException(
                "Need to override execute method to handle multiple inputs",
                "This task has " + str(len(keys)) +
                " inputs and default execute method of Task class cannot handle it.",
                "Override execute and write your own code to handle multiple inputs")

        dataset = inputs.get_interface(keys[0])
        files = dataset.get_all_files()

        output_keys = outputs.get_interface_keys()
        for file in files:
            try:
                if not self.context.file.get_input_file(file).exists():
                    raise PodderTaskException(
                        "File not found",
                        str(self.context.file.get_input_file(file).resolve()) + " doesn't exist")
                result = self.execute_file(str(self.context.file.get_input_file(file)), context)
                result_files = self._normalize_result(result, output_keys)
                for key in output_keys:
                    if not os.path.isfile(result_files[key]):
                        pass
                    outputs.add_file(path=result_files[key], name='output', interface_key=key)
            except PodderTaskException as exception:
                context.logger.critical(exception.full_message)
                for key in output_keys:
                    (outputs.get_interface(key)).add_error(
                        code=exception.code, message=exception.full_message)
            except KeyboardInterrupt as exception:
                raise exception
            except SystemExit as exception:
                context.logger.critical("system exit")
                for key in output_keys:
                    (outputs.get_interface(key)).add_error(code="NONE", message="system exit")
            except Exception as exception:
                podder_exception = PodderTaskException(
                    code="NONE", message="System Error", detail=traceback.format_exc())
                context.logger.critical(str(exception))
                context.logger.critical(traceback.format_exc())
                for key in output_keys:
                    (outputs.get_interface(key)).add_error(
                        code=podder_exception.code, message=podder_exception.full_message)

        return outputs

    @staticmethod
    def _generate_input_data(context: Context, job_id: str) -> DataTransferObjectGroup:
        inputs = None
        if context.mode == MODE.CONSOLE:
            inputs = ArgumentParser(context.config, context.file, job_id).get_input()
        elif context.mode == MODE.PIPELINE:
            pass
        else:
            inputs = DataTransferObjectGroup(
                config=context.config, interface_type=INTERFACE.INPUT, job_id=job_id)

        return inputs

    @staticmethod
    def _normalize_result(result: Any, output_keys):
        result_files = {}
        if isinstance(result, tuple):
            result = list(result)
            if len(result) != len(output_keys):
                PodderTaskException(
                    "Return value count mismatch", "This task has " + str(len(output_keys)) +
                    " outputs but your execute method returned " + str(len(result)) + 'results.',
                    "Confirm with the specification of this task and return right number of result"
                    + " like return a,b,c")
            for index in range(len(output_keys)):
                result_files[output_keys[index]] = result[index]
        elif isinstance(result, dict):
            result_keys = set(result.keys())
            diff = result_keys - set(output_keys)
            if len(diff) != 0:
                PodderTaskException(
                    "Return value keyword mismatch",
                    "This task has outputs named:" + (",".join(output_keys)) +
                    " but your execute method returned " + (",".join(result_keys)) + 'results.',
                    "Confirm with the specification of this task and return with write keys")
            for key in output_keys:
                result_files[key] = result[key]
        elif len(output_keys) != 1:
            PodderTaskException(
                "Return value count mismatch", "This task has " + str(len(output_keys)) +
                " outputs but your execute method returned  only one results",
                "Confirm with the specification of this task and return right number of result" +
                " like return a,b,c")
        else:
            result_files[output_keys[0]] = str(result)

        return result_files
