import json
from enum import Enum


class Status(Enum):
    RESULT = 'RESULT'
    NO_RESULT = 'NO_RESULT'
    NO_METHOD = 'NO_METHOD'
    FAIL = 'FAIL'
    ERROR = 'ERROR'


class Response:
    def __init__(self, request_type, request_reference_id):
        self.request_type = request_type
        self.request_reference_id = request_reference_id
        self._data = None
        self._status = Status.NO_METHOD

    @property
    def status(self):
        return self._status

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if value is not None:
            self._data = value
            self._status = Status.RESULT
        else:
            self._status = Status.NO_RESULT

    @property
    def fails(self):
        if self.status == Status.FAIL:
            return self._data
        return []

    @fails.setter
    def fails(self, value):
        self._data = []
        for fail in value:
            self._data.extend(fail)
        self._status = Status.FAIL

    @property
    def errors(self):
        if self.status == Status.ERROR:
            return self._data
        return []

    @fails.setter
    def errors(self, value):
        self._data = []
        for fail in value:
            self._data.extend(fail)
        self._status = Status.ERROR



class ResponseSerializer:
    def __init__(self, response: Response):
        self._response = response

    def serialize(self):
        data = {
            'status': str(self._response.status)
        }
        if self._response.request_type:
            data['request_type'] = self._response.request_type.decode('utf-8')

        if self._response.request_reference_id:
            data['request_reference_id'] = self._response.request_reference_id.decode('utf-8')

        if self._response.data:
            data['data'] = self._response.data

        return bytes(json.dumps(data), encoding='utf-8')
