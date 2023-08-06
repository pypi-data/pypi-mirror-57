from .response import Response
from .context import Context
from .request import Request


class Application:
    def __init__(self, db, router):
        self._db = db
        self._router = router

    def serve(self, env, start_response):
        if env['REQUEST_METHOD'] == 'POST':
            request = Request(env)
            script = self._router.route(request)
            if script:
                try:
                    result = script.handle(Context(self._db, script.namespace), request)
                except Exception:
                    start_response('500 Bad Request', [('Content-Type', 'application/json')])
                    return []
                else:
                    start_response('200 OK', [('Content-Type', 'application/json')])
                    return [result]
        start_response('404 Not Found', [('Content-Type', 'application/json')])
        return []
