from bbt_root.celery import app
from .service import send

@app.task
def send_feedback(email, text, author):
    send(email, text, author)