import os
from djaio import Djaio

os.environ.setdefault('SETTINGS', 'app.settings.local')
djaio = Djaio()


if __name__ == '__main__':
    djaio.run()
