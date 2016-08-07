import os
import jinja2
import aiohttp_jinja2


def setup(app):
    apps = getattr(app.settings, 'INSTALLED_APPS', [])
    root = getattr(app.settings, 'ROOT_DIR', '')
    paths = []
    for _app in apps:
        tpl_path = os.path.join(root, _app.replace('.', '/'), 'templates')
        if os.path.exists(tpl_path):
            paths.append(tpl_path)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(paths))
