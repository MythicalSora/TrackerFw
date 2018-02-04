import yaml
import aiohttp_jinja2

from aiohttp import web
from trackerfw.route import Route
from trackerfw.module import Module

__all__ = ['Trackers']

class Trackers(Module):
    @property
    def routes(self):
        with open('./trackerfw/config/trackers.yml', 'r') as file:
            config = yaml.load(file.read())

            for route in config['routes']:
                if 'file' in route:
                    handler = self.file_handler(route['file'])
                else:
                    handler = self.cancel_handler

                hostname, path = route['route'].split('/', 1)

                yield Route(
                    handler,
                    hostname=hostname,
                    path='/' + path
                )

    async def cancel_handler(self, request):
        return web.HTTPBadRequest()

    def file_handler(self, filename):
        content_type = 'text/plain'

        if '.js' in filename:
            content_type = 'text/javascript'

        async def handler(request):
            return web.Response(
                text=aiohttp_jinja2.render_string(filename, request, {}),
                content_type=content_type
            )

        return handler
