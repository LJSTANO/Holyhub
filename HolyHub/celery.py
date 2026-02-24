from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HolyHub.settings')

app = Celery('HolyHub')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-devotion-every-day': {
        'task': 'sermons.tasks.send_daily_devotion',
        'schedule': crontab(hour=6, minute=00),
    },
}
