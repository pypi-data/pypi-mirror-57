from descarteslabs.common.proto import errors_pb2


class JobComputeError(Exception):
    def __init__(self, job):
        self._id = job.id
        self._code = errors_pb2.ErrorCode.Name(job._message.error.code)
        self._message = job._message.error.message

        super(JobComputeError, self).__init__(
            'Job("{}") failed with: code={}, message="{}"'.format(
                self._id, self._code, self._message
            )
        )

    @property
    def code(self):
        return self._code

    @property
    def id(self):
        return self._id

    @property
    def message(self):
        return self._message


class JobOOM(JobComputeError):
    pass


class JobInvalid(JobComputeError):
    pass


class JobDeadlineExceeded(JobComputeError):
    pass


class JobTerminated(JobComputeError):
    pass


class TimeoutError(Exception):
    pass


ERRORS = {
    errors_pb2.ERROR_DEADLINE: JobDeadlineExceeded,
    errors_pb2.ERROR_INVALID: JobInvalid,
    errors_pb2.ERROR_OOM: JobOOM,
    errors_pb2.ERROR_TERMINATED: JobTerminated,
    errors_pb2.ERROR_UNKNOWN: JobComputeError,
}
