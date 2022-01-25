from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab
from datetime import datetime, timedelta

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leavestracker.settings.local")

app = Celery('leavestracker')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'add-every-morning  ': {
        'task': 'leavestracker.apps.leaves.tasks.send_notification',
        'schedule': crontab(minute=0 , hour=9),
    }
}

app.conf.timezone = 'Asia/Kolkata'

app.autodiscover_tasks()
