from aiohttp import web
from trackerfw.module import Module
from trackerfw.route import Route

__all__ = ['UrlPatterns']

class UrlPatterns(Module):
    @property
    def routes(self):
        yield Route(
            self.handler,
            path='/patterns'
        )

    async def handler(self, request):
        return web.json_response([
            pattern for pattern in [
                route.pattern for route in request.match_info.app.router.routes
            ] if pattern != None
        ], headers={
            'Access-Control-Allow-Origin': '*'
        })
