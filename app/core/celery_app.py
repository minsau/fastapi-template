from celery import Celery
from app.core.config import settings

app = Celery("worker", broker=settings.CELERY_BROKER_URL, include=["app.tasks"])

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'app.tasks.calculate_account_history_by_account',
        'schedule': 30.0,
    },
}
app.conf.timezone = 'UTC'