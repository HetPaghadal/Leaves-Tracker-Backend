from __future__ import absolute_import, unicode_literals

from celery import Celery
from datetime import datetime, timedelta

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leavestracker.settings.local")

app = Celery('leavestracker')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'leavestracker.apps.leaves.tasks.send_notification',
        'schedule': 10,
    }
}

app.conf.timezone = 'UTC'

app.autodiscover_tasks()
