from django import template
from ..models import BooksForFree

register = template.Library()


@register.simple_tag()
def get_reviews(slug):
    return BooksForFree.objects.get(slug=slug)