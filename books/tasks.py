from celery import shared_task

from books.models import BooksForBuy
from .service import send
from .logic import end_goal, get_emails, send_all_emails

@shared_task
def check_buy_books():
    books = BooksForBuy.objects.all()

    for book in books:
        if end_goal(book.current_goal, book.finish_goal):
            emails = get_emails(book)
            send(emails, book.title)
            send_all_emails(emails)
            book.delete()

        else:
            pass