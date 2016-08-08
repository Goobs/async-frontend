from djaio.core.urlconf import url
from .views import TestView, SomeView


url('GET', '/', TestView, name='index')
url('GET', '/some', SomeView, name='some')
