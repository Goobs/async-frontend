from aiohttp import web
from djaio.core.server import init_app


class Djaio(object):

    def __init__(self):
        self.app = init_app()

    def run(self):
        web.run_app(self.app)
