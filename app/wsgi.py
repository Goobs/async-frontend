import os
from djaio import Djaio

os.environ.setdefault('SETTINGS', 'app.settings.local')
djaio = Djaio()

app = djaio.app
