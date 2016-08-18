from djaio.core.views import TemplateView, RemoteContextMixin
from djaio_spf.views import SPFTemplateMixin


class TestView(RemoteContextMixin, TemplateView):
    data_url_map = (
        ('data1', 'https://realty.rambler.ru/api/v1/offers/?per_page=2&category_id=7&site_region_id=1'),
        ('data2', 'https://realty.rambler.ru/api/v1/offers/?per_page=2&category_id=11&site_region_id=1'),
        ('data3', 'https://realty.rambler.ru/api/v1/offers/?per_page=2&category_id=7&site_region_id=2'),
        ('data4', 'https://realty.rambler.ru/api/v1/offers/?per_page=2&category_id=11&site_region_id=2'),
    )
    template_name = 'serp/index.html'


class SomeView(SPFTemplateMixin):
    template_name = 'spf/index.html'
    template_map = (
        ('body/main-block', 'spf/includes/main.html'),
        ('body/aside-block', 'spf/includes/aside.html'),
        ('footer', 'spf/includes/footer.html'),
    )

    async def get_context_data(self, *args, **kwargs):
        context = await super(SomeView, self).get_context_data(*args, **kwargs)
        context['getparam'] = self.request.GET.get('test')
        return context


class SomeOtherView(SomeView):
    async def get_context_data(self, *args, **kwargs):
        context = await super(SomeView, self).get_context_data(*args, **kwargs)
        context['getparam'] = self.request.GET.get('test')
        context['asd'] = 'asd'
        context['qwe'] = '123'
        return context
