import re
from .request import Request


class Route:
    def __init__(self, namespace, script):
        self.namespace = namespace
        self.script = script


class Router:
    def __init__(self, routing):
        self._routing = routing

    def route(self, request: Request):
        for url, route in self._routing:
            if re.match(url, request.request_uri):
                return route
        return None
