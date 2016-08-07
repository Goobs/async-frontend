from core.views import TemplateView, RemoteContextMixin


class TestView(RemoteContextMixin, TemplateView):
    data_url_map = (
        ('data1', 'https://realty.rambler.ru/api/v1/offers/?per_page=100&category_id=7&site_region_id=1'),
        ('data2', 'https://realty.rambler.ru/api/v1/offers/?per_page=100&category_id=11&site_region_id=1'),
        ('data3', 'https://realty.rambler.ru/api/v1/offers/?per_page=100&category_id=7&site_region_id=2'),
        ('data4', 'https://realty.rambler.ru/api/v1/offers/?per_page=100&category_id=11&site_region_id=2'),
    )
    template_name = 'serp/index.html'


class SomeView(TemplateView):
    template_name = 'serp/some.html'
