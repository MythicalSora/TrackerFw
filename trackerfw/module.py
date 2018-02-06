import aiohttp_jinja2

from aiohttp import web

class Module(object):
    def __init__(self, basedir):
        self.basedir = basedir

    def routes():
        raise Exception('please override `routes`')

    async def handler(request):
        pass
