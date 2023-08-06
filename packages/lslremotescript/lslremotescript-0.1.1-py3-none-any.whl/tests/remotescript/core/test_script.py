import io
import json
import pytest
from remotescript.core.script import ScriptController
from remotescript.core.context import Context
from remotescript.core.request import Request
from remotescript.core.exceptions import ScriptError, ScriptFail
from .utils import InMemoryDB


class DummyScript:
    def on_rez(self, context, request):
        return {
            'code': [
                'CALL llOwnerSay("hastalvista")'
            ]
        }
        pass

    def on_empty(self, context, request):
        pass

    def on_faulty(self, context, request):
        raise ScriptError('something happened')

    def on_faultyfail(self, context, request):
        raise ScriptFail('something happened')


@pytest.fixture
def dummy_script():
    return DummyScript()


@pytest.fixture
def context():
    return Context(InMemoryDB, "dummy_namespace")


@pytest.fixture
def request_factory():
    def request_fact(post_data: dict):
        _input = bytes('&'.join([f'{k}={v}' for k, v in post_data.items()]), encoding='utf-8')
        return Request({
            'CONTENT_TYPE': 'application/x-www-form-urlencoded',
            'wsgi.input': io.BytesIO(_input)
        })
    return request_fact


class TestScriptController:
    def test_should_return_script_result(self, dummy_script, context, request_factory):
        post_data = {
            'request_type': 'on_rez',
            'request_reference_id': 'dummy',
        }
        request = request_factory(post_data)
        controller = ScriptController("dummy_namespace", dummy_script)
        response = controller.handle(context, request)
        response = json.loads(response.decode('utf-8'))
        assert 'status' in response
        assert response['status'] == 'Status.RESULT'
        assert 'request_type' in response
        assert response['request_type'] == post_data['request_type']
        assert 'request_reference_id' in response
        assert response['request_reference_id'] == post_data['request_reference_id']
        assert 'data' in response
        assert response['data'] == dummy_script.on_rez(context, request)

    def test_request_reference_id_is_not_mandatory(self, dummy_script, context, request_factory):
        post_data = {
            'request_type': 'on_rez',
        }
        request = request_factory(post_data)
        controller = ScriptController("dummy_namespace", dummy_script)
        response = controller.handle(context, request)
        response = json.loads(response.decode('utf-8'))
        assert 'status' in response
        assert response['status'] == 'Status.RESULT'
        assert 'request_type' in response
        assert response['request_type'] == post_data['request_type']
        assert 'request_reference_id' not in response
        assert 'data' in response
        assert response['data'] == dummy_script.on_rez(context, request)

    def test_request_type_is_mandatory(self, dummy_script, context, request_factory):
        pass
        post_data = {}
        request = request_factory(post_data)
        controller = ScriptController("dummy_namespace", dummy_script)
        response = controller.handle(context, request)
        response = json.loads(response.decode('utf-8'))
        assert response.get('status') == 'Status.FAIL'
        assert 'request_type' in response.get('data', [])

    def test_should_return_no_method_status_if_method_is_not_supported(self, dummy_script, context, request_factory):
        post_data = {
            'request_type': 'on_rez_not_existing',
            'request_reference_id': 'dummy',
        }
        request = request_factory(post_data)
        controller = ScriptController("dummy_namespace", dummy_script)
        response = controller.handle(context, request)
        response = json.loads(response.decode('utf-8'))
        assert response.get('status') == 'Status.NO_METHOD'
        assert 'data' not in response

    def test_should_return_no_result_status_if_result_is_empty(self, dummy_script, context, request_factory):
        post_data = {
            'request_type': 'on_empty',
            'request_reference_id': 'dummy',
        }
        request = request_factory(post_data)
        controller = ScriptController("dummy_namespace", dummy_script)
        response = controller.handle(context, request)
        response = json.loads(response.decode('utf-8'))
        assert response.get('status') == 'Status.NO_RESULT'
        assert 'data' not in response

    def test_should_return_error_when_any_unhandled_script_error_happen(self, dummy_script, context, request_factory):
        post_data = {
            'request_type': 'on_faulty',
            'request_reference_id': 'dummy',
        }
        request = request_factory(post_data)
        controller = ScriptController("dummy_namespace", dummy_script)
        response = controller.handle(context, request)
        response = json.loads(response.decode('utf-8'))
        assert response.get('status') == 'Status.ERROR'
        assert 'data' in response

    def test_should_return_fail_when_any_unhandled_script_fail_happen(self, dummy_script, context, request_factory):
        post_data = {
            'request_type': 'on_faultyfail',
            'request_reference_id': 'dummy',
        }
        request = request_factory(post_data)
        controller = ScriptController("dummy_namespace", dummy_script)
        response = controller.handle(context, request)
        response = json.loads(response.decode('utf-8'))
        assert response.get('status') == 'Status.FAIL'
        assert 'data' in response
