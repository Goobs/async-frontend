from .base import *

DEBUG = True
DEBUG_TOOLBAR = True

STATIC_URL = '/assets'
STATIC_PATH = os.path.join(ROOT_DIR, 'app', 'static', 'dist')
