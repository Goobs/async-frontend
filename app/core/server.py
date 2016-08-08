import os
import importlib
from aiohttp import web
import aiohttp_debugtoolbar
import app.core.settings as _settings
from app.core import urlconf
from app.core import templating
from app.core import assets


def get_settings():
    settings_module = os.environ.get('SETTINGS', 'app.settings')
    settings = None
    try:
        settings = importlib.import_module(settings_module)
    except:
        print('Settings module not found. Using the default one.')

    if settings:
        for k, v in settings.__dict__.items():
            setattr(_settings, k, v)
    return _settings


def discover_urls(app):
    settings = getattr(app, 'settings', None)
    if settings is None:
        return
    for app in settings.INSTALLED_APPS:
        importlib.import_module('{}.urls'.format(app))


def init_app():
    _settings = get_settings()
    middlewares = []

    if _settings.DEBUG and _settings.DEBUG_TOOLBAR:
        middlewares.append(aiohttp_debugtoolbar.middleware)

    app = web.Application(middlewares=middlewares, debug=_settings.DEBUG)
    app.settings = _settings
    discover_urls(app)
    urlconf.setup(app)
    templating.setup(app)
    assets.setup(app)

    if app.settings.DEBUG:
        if _settings.DEBUG_TOOLBAR:
            aiohttp_debugtoolbar.setup(app)
        app.router.add_static(_settings.STATIC_URL, _settings.STATIC_PATH)
    return app
