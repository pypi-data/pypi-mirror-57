from collections import namedtuple
from .errorcodes import CODE_ERROR_MISSING_PARAMETER


ErrorCode = namedtuple('ErrorCode', ['param_name', 'code', 'message'])


class StandardScriptValidator:
    def __init__(self):
        self.errors = []

    def validate(self, request):
        if b'request_type' not in request.data:
            self.errors.append(ErrorCode('request_type', CODE_ERROR_MISSING_PARAMETER, 'is mandatory'))

        return self.errors
