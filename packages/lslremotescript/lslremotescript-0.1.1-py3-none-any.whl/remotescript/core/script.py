from .exceptions import ScriptError, ScriptFail
from .request import Request
from .response import Response, ResponseSerializer
from .context import Context
from .validators import StandardScriptValidator


class ScriptController:
    def __init__(self, namespace, script, validators=None):
        self._script = script
        self._namespace = namespace
        self._validators = validators or []

    def _validate(self, request):
        validators = [StandardScriptValidator()]
        validators.extend(self._validators)
        errors = []
        for validator in validators:
            errors.extend(validator.validate(request))
        return errors

    def handle(self, context: Context, request: Request):

        request_type = request.data.get(b'request_type', [None])[0]
        request_id = request.data.get(b'request_reference_id', [None])[0]
        response = Response(request_type, request_id)
        errors = self._validate(request)
        if errors:
            response.fails = errors
            return ResponseSerializer(response).serialize()

        if request_type and request_type.lower().startswith(b"on_"):
            request_type = request_type.lower().decode('utf-8')
            if hasattr(self._script, request_type):
                fun = getattr(self._script, request_type)
                try:
                    response.data = fun(context, request)
                except ScriptError as e:
                    response.errors = [(None, e.error_code, str(e))]
                    return ResponseSerializer(response).serialize()
                except ScriptFail as e:
                    response.fails = [(None, e.error_code, str(e))]
                    return ResponseSerializer(response).serialize()

        return ResponseSerializer(response).serialize()

    @property
    def namespace(self):
        return self._namespace
