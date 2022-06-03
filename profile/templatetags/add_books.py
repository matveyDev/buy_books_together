from django import template

from ..forms import BookForFreeTagForm, BookForBuyTagForm

register = template.Library()


@register.inclusion_tag('add_free_book/tags/form.html')
def add_free_book_form():
    return {
        'books_for_free_form': BookForFreeTagForm(),
    }

@register.inclusion_tag('add_buy_book/tags/form.html')
def add_buy_book_form():
    return {
        'books_for_buy_form': BookForBuyTagForm(),
    }