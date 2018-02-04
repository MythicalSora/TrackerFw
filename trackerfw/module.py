import aiohttp_jinja2

from aiohttp import web

class Module(object):
    def routes():
        raise Exception('please override `routes`')

    def serve_file(self, filename, content_type):
        async def handler(request):
            return web.Response(
                text=aiohttp_jinja2.render_string(filename, request, {}),
                content_type=content_type
            )

        return handler

    async def handler(request):
        pass
