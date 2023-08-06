import json
import traceback

from podder_task_foundation.objects.data_transfer_object_group import DataTransferObjectGroup
from podder_task_foundation.objects.data_transfer_objects import Dataset

from ..exceptions import PodderTaskException
from ..objects.data_transfer_object_group.interface_type import INTERFACE
from ..objects.errors import Error
from ..task import Task
from .protos import pipeline_framework_pb2, pipeline_framework_pb2_grpc


class TaskGRPCWrapper(pipeline_framework_pb2_grpc.PodderTaskApiServicer):
    def __init__(self, task: Task):
        self._task = task

    def execute(self, request, context) -> pipeline_framework_pb2.DataTransferObjectGroup:
        dag_id = request.dag_id
        job_id = request.job_id
        try:
            input_ = self._convert_request_to_input(request)
            output = self._task.handle(job_id=job_id, dag_id=dag_id, input_=input_)
            task_data = self._convert_output_to_response(dag_id, job_id, output)
        except Exception as e:
            self._task.context.logger.error(traceback.format_exc())
            return self._make_error_task_data(dag_id, job_id, e)

        return task_data

    def _convert_request_to_input(self, task_data: pipeline_framework_pb2.DataTransferObjectGroup
                                  ) -> DataTransferObjectGroup:
        input_ = DataTransferObjectGroup(
            config=self._task.context.config, interface_type=INTERFACE.INPUT)
        for key in task_data.data:
            job_data = task_data.data[key]
            interfaces = input_.get_interface(key)

            interfaces.job_id = task_data.job_id

            for property_key, value in json.loads(job_data.properties):
                interfaces.set_property(property_key, value)

            for error in json.loads(job_data.errors):
                interfaces.add_error(error['code'], error['messahe'])

            for data in json.loads(job_data.datasets):
                interfaces.add_data(data)

        return input_

    @staticmethod
    def _convert_output_to_response(dag_id: str, job_id: str, output: DataTransferObjectGroup
                                    ) -> pipeline_framework_pb2.DataTransferObjectGroup:
        task_data = pipeline_framework_pb2.DataTransferObjectGroup()
        task_data.dag_id = dag_id
        task_data.job_id = job_id

        for key in output.get_interface_keys():
            interface = output.get_interface(key)

            job_data = pipeline_framework_pb2.DataTransferObject()

            output_dict = interface.to_dict()
            job_data.datasets = json.dumps(output_dict['dataset'])
            job_data.properties = json.dumps(output_dict['properties'])
            task_data.data[key].CopyFrom(job_data)

        return task_data

    @staticmethod
    def _make_error_task_data(dag_id: str, job_id: str,
                              e: Exception) -> pipeline_framework_pb2.DataTransferObjectGroup:
        task_data = pipeline_framework_pb2.DataTransferObjectGroup()
        task_data.dag_id = dag_id
        task_data.job_id = job_id

        if isinstance(e, PodderTaskException):
            error = Error(code=e.code, message=e.full_message)
        else:
            message = str(e)
            error = Error(code=0, message=message)

        task_data.errors = json.dumps([error])

        return task_data
