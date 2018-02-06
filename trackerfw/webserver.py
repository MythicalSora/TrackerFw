import os
import ssl
import jinja2
import importlib.util
import aiohttp_jinja2

from aiohttp import web
from urllib.parse import unquote, urlparse
from trackerfw.router import Router

class Webserver(object):
    def __init__(self):
        self._modules = None
        self.router = Router()
        self._ssl_context = None
        self.basedir = os.path.dirname(os.path.realpath(__file__)) + '/'

    def _load_modules(self, name):
        spec = importlib.util.spec_from_file_location(
            name,
            self.basedir + '/modules/' + name + '.py'
        )
        py_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(py_module)

        for key in py_module.__all__:
            yield getattr(py_module, key)(self.basedir)

    @property
    def ssl_context(self):
        if self._ssl_context == None:
            self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            self._ssl_context.load_cert_chain(
                self.basedir + 'certs/cert.pem',
                self.basedir + 'certs/key.pem'
            )

        return self._ssl_context

    @property
    def modules(self):
        if self._modules == None:
            self._modules = []

            for file in os.listdir(self.basedir + '/modules/'):
                if '__' in file:
                    continue

                self._modules += [m for m in self._load_modules(file[:-3])]

        return self._modules

    @web.middleware
    async def reroute(self, request, handler):
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

    def listen(self, host, port):
        for module in self.modules:
            for route in module.routes:
                self.router.routes.append(route)

        app = web.Application(
            router=self.router,
            middlewares=[
                self.reroute
            ]
        )

        aiohttp_jinja2.setup(
            app,
            loader=jinja2.PackageLoader('trackerfw', 'templates')
        )

        web.run_app(
            app,
            port=port,
            host=host,
            ssl_context=self.ssl_context
        )
