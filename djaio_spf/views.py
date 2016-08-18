import json
import asyncio
import aiohttp_jinja2
from aiohttp import web
from djaio.core.views import BaseContextmixin, TemplateView
from djaio.core.utils import gather_map


class SPFTemplateMixin(TemplateView):
    template_map = (
                       ('head', ''),
                       ('body', ''),
                       ('foot', ''),
    )
    _template_map_cache = None

    def get_template_map(self):
        return self.template_map

    def _get_template_map_cached(self):
        if not self._template_map_cache:
            self._template_map_cache = self.get_template_map()
        return self._template_map_cache

    async def render_part(self, part, context):
        _template = None
        for k, v in self._get_template_map_cached():
            if v == part:
                _template = v
                break
        if not _template:
            return ''
        return aiohttp_jinja2.render_string(
            _template,
            self.request,
            context
        )

    async def render_parts(self, context):
        spf_dict = {}
        _parts = await gather_map(self._get_template_map_cached(), self.render_part, context=context)
        for k, item in _parts:
            _path = k.split('/')
            _l = len(_path)
            if _l == 1:
                spf_dict[_path[0]] = item
            elif _l == 2:
                if not spf_dict.get(_path[0]):
                    spf_dict[_path[0]] = {}
                spf_dict[_path[0]][_path[1]] = item
        return spf_dict

    async def get(self):
        _spf = self.request.GET.get('spf')
        context = await self.get_context_data()
        if _spf == 'navigate':
            return web.Response(
                body=bytes(json.dumps(await self.render_parts(context)), encoding='utf-8'),
                content_type='application/json'
            )
        body = await self.render()
        return body
