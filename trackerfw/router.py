from aiohttp.abc import AbstractRouter

from trackerfw.route import Route
from trackerfw.match_info import MatchInfo

class Router(AbstractRouter):
    def __init__(self):
        super().__init__()

        self.routes = []

    async def resolve(self, request):
        for route in self.routes:
            if route.matches(request):
                return MatchInfo(route)

        return MatchInfo()

    def add(self, handler, **kwargs):
        self.routes.append(Route(handler, **kwargs))
