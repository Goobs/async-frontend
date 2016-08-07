import asyncio
import aiohttp
from aiohttp import web
import aiohttp_jinja2


class BaseContextmixin(object):
    async def get_context_data(self, *args, **kwargs):
        context = {}
        return context


class RemoteContextMixin(BaseContextmixin):
    data_url_map = tuple()

    def get_data_url_map(self):
        return self.data_url_map

    async def get_remote_data(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    raise web.HTTPBadGateway
                try:
                    return await resp.json()
                except:
                    raise web.HTTPBadGateway

    async def get_context_data(self, *args, **kwargs):
        context = await super(RemoteContextMixin, self).get_context_data(*args, **kwargs)
        _keys = []
        _coros = []

        for key, url in self.get_data_url_map():
            _keys.append(key)
            _coros.append(self.get_remote_data(url))
        _results = await asyncio.gather(*_coros)
        context.update(dict(zip(_keys, _results)))
        return context


class TemplateView(BaseContextmixin, web.View):
    template_name = None

    def get_template_name(self):
        return self.template_name

    async def render(self):
        return aiohttp_jinja2.render_template(
            self.get_template_name(),
            self.request,
            await self.get_context_data()
        )

    async def get(self):
        body = await self.render()
        return body

