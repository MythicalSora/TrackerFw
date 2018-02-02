from aiohttp import web
from trackerfw.module import Module
from trackerfw.route import Route

__all__ = ['TraceDoubler']

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
