import os
from aiohttp import web
from core.server import init_app


if __name__ == '__main__':
    os.environ.setdefault('SETTINGS', 'app.settings.local')
    app = init_app()
    web.run_app(app)
