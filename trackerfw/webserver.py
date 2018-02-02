import os
import importlib.util

from aiohttp import web
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

    app = web.Application(
        router=router
    )

    return app