import os
import ssl
import jinja2
import importlib.util
import aiohttp_jinja2

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

def make_app():
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
                method=request.method,
                scheme=uri.scheme,
                host=uri.netloc.split(':')[0]
            )

            router = request.match_info.current_app.router
            match_info = await router.resolve(new_request)

            return await match_info.handler(new_request)

        return await handler(request)

    app = web.Application(
        router=router,
        middlewares=[
            reroute
        ]
    )

    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('trackerfw', 'templates')
    )

    return app

ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
ssl_ctx.load_cert_chain(
    './certs/cert.pem',
    './certs/key.pem'
)

web.run_app(
    make_app(),
    port=9999,
    ssl_context=ssl_ctx,
    host='localhost',
)
