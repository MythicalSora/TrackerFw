from contextlib import contextmanager
from aiohttp.abc import AbstractMatchInfo
from aiohttp.web_exceptions import HTTPNotFound

class MatchInfo(AbstractMatchInfo):
    def __init__(self, route=None):
        super().__init__()

        self.app = None
        self._route = route
        self._current_app = None

    def add_app(self, app):
        self.app = app

    def freeze(self): pass

    def get_info(self):
        if self._route == None:
            return {}

        return self._route.__dict__

    @contextmanager
    def set_current_app(self, app):
        yield
        self._current_app = app

    @property
    def expect_handler(self):
        return None

    @property
    def http_exception(self):
        if self._route == None:
            return HTTPNotFound()

        return None

    @property
    def current_app(self):
        return self._current_app

    @property
    def apps(self):
        if self.app == None:
            return []

        return [self.app]

    @property
    def handler(self):
        if self._route == None:
            return None

        return self._route.handler
