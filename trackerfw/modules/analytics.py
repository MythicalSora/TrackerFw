import aiohttp_jinja2

from aiohttp import web
from trackerfw.route import Route
from trackerfw.module import Module

__all__ = ['CancelPixelsBeacons', 'StaticScripts']

class CancelPixelsBeacons(Module):
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

        # MarkMonitor
        yield Route(
            self.handler,
            hostname='beacon.krxd.net',
            path='/*'
        )

    async def handler(self, request):
        return web.HTTPBadRequest()

class StaticScripts(Module):
    @property
    def routes(self):
        # Gigya
        yield Route(
            self.serve_file('gigya.js', 'text/javascript'),
            hostname='cdns.gigya.com',
            path='/js/gigya.js'
        )

        # Google Tag Manager
        yield Route(
            self.serve_file('gtm.js', 'text/javascript'),
            hostname='www.googletagmanager.com',
            path='/gtm.js'
        )
