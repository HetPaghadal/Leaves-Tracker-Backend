from __future__ import absolute_import, unicode_literals
from leavestracker.apps.leaves.models import Leaves
from celery.decorators import task

@task
def send_notification():
    Leaves.send_notification()
