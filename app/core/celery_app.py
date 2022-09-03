from celery import Celery

from app.core.config import settings

app = Celery("worker", broker=settings.CELERY_BROKER_URL, include=["app.tasks"])

app.conf.beat_schedule = {
    "add-every-30-seconds": {
        "task": "app.tasks.send_user_invitation",
        "schedule": 30.0,  # 30 seconds
    },
}
app.conf.timezone = "UTC"
