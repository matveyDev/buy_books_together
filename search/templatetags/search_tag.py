from django import template
from ..forms import SearchForm

register = template.Library()


@register.inclusion_tag('search/tags/form.html')
def search_form():
    return {'search_form': SearchForm()}