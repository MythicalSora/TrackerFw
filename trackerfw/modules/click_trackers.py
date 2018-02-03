import aiohttp_jinja2

from aiohttp import web
from trackerfw.module import Module
from trackerfw.route import Route

__all__ = ['TraceDoubler', 'MailRD']

class TraceDoubler(Module):
    @property
    def routes(self):
        yield Route(
            self.handler,
            hostname='clk.tradedoubler.com',
            path='/click'
        )

    @aiohttp_jinja2.template('redirect.html')
    async def handler(self, request):
        return {
            'redirect_url': request.query['url']
        }

class MailRD(Module):
    @property
    def routes(self):
        yield Route(
            self.handler,
            hostname='click.mailrd.net',
            path='/'
        )

    async def handler(self, request):
        return web.HTTPTemporaryRedirect(request.query['href'])
