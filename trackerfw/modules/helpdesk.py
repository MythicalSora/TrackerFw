import aiohttp_jinja2

from aiohttp import web
from trackerfw.route import Route
from trackerfw.module import Module

__all__ = ['StaticScripts']

class StaticScripts(Module):
    @property
    def routes(self):
        yield Route(
            self.serve_file('zopim.js', 'text/javascript'),
            hostname='*.zopim.com',
            path='/'
        )
