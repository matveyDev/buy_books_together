import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bbt_root.settings')

app = Celery('bbt_root')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-notificationsails': {
        'task': 'books.tasks.check_buy_books',
        # every 30 sec
        'schedule': 30,
    }
}