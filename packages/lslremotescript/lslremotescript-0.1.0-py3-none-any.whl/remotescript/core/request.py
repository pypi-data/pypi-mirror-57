import logging
from urllib.parse import parse_qs


# TODO: to customize logging to see debug
logger = logging.getLogger(__name__)


class Request:
    def __init__(self, env: dict):
        self._env = env
        for k, v in env.items():
            logger.debug(f"{k} = {v}")
            setattr(self, k.lower(), v)

        if env['CONTENT_TYPE'] == 'application/x-www-form-urlencoded':
            self.data = parse_qs(env['wsgi.input'].read())


