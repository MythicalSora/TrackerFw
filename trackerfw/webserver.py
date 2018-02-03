import os
import importlib.util

from aiohttp import web
from urllib.parse import unquote, urlparse
from .router import Router

def load_modules(basedir, name):
    spec = importlib.util.spec_from_file_location(
        name,
        basedir + '/modules/' + name + '.py'
    )
    py_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(py_module)

    for key in py_module.__all__:
        yield getattr(py_module, key)()

def discover():
    basedir = os.path.dirname(os.path.realpath(__file__))

    for file in os.listdir(basedir + '/modules/'):
        if '__' in file:
            continue

        yield from load_modules(basedir, file[:-3])

def run(argv):
    router = Router()

    for module in discover():
        for route in module.routes:
            router.routes.append(route)

    @web.middleware
    async def reroute(request, handler):
        if request.path == '/$route':
            raw_uri = unquote(request.query['uri'])
            uri = urlparse(raw_uri)
            new_request = request.clone(
                rel_url=raw_uri,
                method='GET',
                scheme=uri.scheme,
                host=uri.netloc.split(':')[0]
            )

            router = request.match_info.app.router
            match_info = await router.resolve(new_request)

            return await match_info.handler(new_request)

        return await handler(request)

    app = web.Application(
        router=router,
        middlewares=[
            reroute
        ]
    )

    return app