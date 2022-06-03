from django.core.mail import send_mail

from books.models import BooksForBuy
from .config import SITE_URL

def send(user, book_pk, amount, emails):
    book = BooksForBuy.objects.get(pk=book_pk)
    send_mail(
        f'{user} invest.',
        f'{user} invest in {book.title} {amount} RUB !\n {SITE_URL}{book.get_absolute_url()}',
        'noreplyarenda@gmail.com',
        emails,
        fail_silently=True
    )