from djaio.core.urlconf import url
from .views import TestView, SomeView, SomeOtherView


url('GET', '/', TestView, name='index')
url('GET', '/some', SomeView, name='some')
url('GET', '/someother', SomeOtherView, name='someother')
