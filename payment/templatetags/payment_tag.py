from django import template
from ..forms import PaymentTagForm

register = template.Library()


@register.inclusion_tag('payment/tags/form.html')
def payment_form(book_pk):
    return {
        'payment_form': PaymentTagForm(),
        'book_pk': book_pk,
    }