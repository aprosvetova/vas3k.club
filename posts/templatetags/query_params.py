from copy import deepcopy
from urllib.parse import urlencode

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def append_query_param(context, **kwargs):
    query_params = deepcopy(context.request.GET.dict())
    query_params.update(kwargs)
    return "?" + urlencode(query_params)
