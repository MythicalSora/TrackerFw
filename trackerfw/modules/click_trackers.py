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

    async def handler(self, request):
        return web.HTTPTemporaryRedirect(request.query['url'])

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
