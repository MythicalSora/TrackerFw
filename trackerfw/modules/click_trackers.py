import aiohttp_jinja2

from aiohttp import web
from trackerfw.module import Module
from trackerfw.route import Route
from trackerfw.tracker_utils import top_level_extensions

__all__ = ['RedirectUris']

class RedirectUris(Module):
    @property
    def routes(self):
        # TradeDoubler
        yield Route(
            self.handler,
            hostname='clk.tradedoubler.com',
            path='/click'
        )

        # Google
        for ext in top_level_extensions:
            yield Route(
                self.handler,
                hostname='www.google' + ext,
                path='/url'
            )

        # MailRD
        yield Route(
            self.handler,
            hostname='click.mailrd.net',
            path='/'
        )

    @aiohttp_jinja2.template('redirect.html')
    async def handler(self, request):
        query_keys = [
            'url',
            'href'
        ]

        for key in query_keys:
            if key in request.query:
                return {
                    'redirect_url': request.query[key]
                }

        return {
            'url': str(request.url),
            'redirect_url': None,
        }
