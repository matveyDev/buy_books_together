from bbt_root.celery import app
from .service import send

@app.task
def send_contact(email):
    send(email)