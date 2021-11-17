import os
from celery.schedules import crontab
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kavKev_Site.settings')

app = Celery('kavKev_Site')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    "annul-day-qr": {
        "task": "mainapp.tasks.annul_day_qr",
        "schedule": crontab(minute=0, hour=0)#
    }
}