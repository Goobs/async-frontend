import os

ROOT_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
TEMPLATES_DIR = os.path.join(ROOT_DIR, 'app', 'templates')
DEBUG = False

INSTALLED_APPS = [
    'app.serp'
]
WEBPACK_MANIFEST_PATH = os.path.join(ROOT_DIR, 'app', 'static', 'manifest.json')
