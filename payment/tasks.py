from django.contrib.auth import get_user_model

from books.models import BooksForBuy
from bbt_root.celery import app
from .service import send
from .logic import get_emails

@app.task()
def send_mails(user, book_pk, amount):
    emails = get_emails(book_pk)
    send(user, book_pk, amount, emails)

@app.task()
def add_user_in_buyers(book_pk, user_pk):
    book = BooksForBuy.objects.get(pk=book_pk)
    user = get_user_model().objects.get(pk=user_pk)
    book.buyers.add(user)