import aiohttp_jinja2

from aiohttp import web
from trackerfw.route import Route

__all__ = ['GoogleTagManager', 'CancelPixels']

class CancelPixels(object):
    @property
    def routes(self):
        # Google tag services
        yield Route(
            self.handler,
            hostname='www.googletagservices.com',
            path='/tag/*'
        )

        # ActiveCampaign
        yield Route(
            self.handler,
            hostname='trackcmp.net',
            path='/visit'
        )

    async def handler(self, request):
        return web.Response(text='')

class GoogleTagManager(object):
    @property
    def routes(self):
        yield Route(
            self.handler,
            hostname='www.googletagmanager.com',
            path='/gtm.js'
        )

    async def handler(self, request):
        return web.Response(
            text=aiohttp_jinja2.render_string('gtm.js', request, {}),
            content_type='text/javascript'
        )
