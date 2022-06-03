from bbt_root.celery import app

from .service import send_notification_free_book, send_notification_buy_book

@app.task
def email_free_book(user):
    send_notification_free_book(user)

@app.task
def email_buy_book(user):
    send_notification_buy_book(user)