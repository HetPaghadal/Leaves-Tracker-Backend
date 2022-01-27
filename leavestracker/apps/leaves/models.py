from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.db.models import Q
from django.utils.timezone import datetime
from leavestracker.apps.employees.models import CustomUser
from leavestracker.apps.leaves import constants as const
from leavestracker.settings import local

import datetime
import json
import os
import requests

class Leaves(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_date = models.DateField(blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)
    reason = models.CharField(max_length = 30, null = True)

    def clean(self):
        error = []
        if self.start_date>self.end_date:
            error.append(const.INVALID_DATE_RAISE_ERROR)
        if Leaves.objects.filter(Q(user_id=self.user_id) & (Q(start_date__range=[self.start_date,self.end_date]) | Q(end_date__range=[self.start_date,self.end_date]))).exists():
            error.append(const.DUPLICATE_LEAVE_RAISE_ERROR)

        if error:
            raise ValidationError(error)

    @classmethod
    def get_leaves_for_today(cls):
        today = datetime.date.today()

        queryset = cls.objects.filter(
            start_date__lte=today, end_date__gte=today
        )
        return queryset

    @classmethod
    def create_slack_notification(cls, leaves):
        message = const.SLACK_MSG_HEADER
        for leave in leaves:
            message = message + '\n'
            message = message + str(leave.user.first_name) + ' ' + str(leave.user.last_name)+ ' ' + str(leave.user.email) + ' ' + ' (Reason:' + str(leave.reason) + ')'

        payload = {
            "text": message
        }
        response = requests.post(os.environ.get('SLACK_URL'), data=json.dumps(payload))

    @classmethod
    def send_notification(cls):
        queryset = cls.get_leaves_for_today()
        cls.create_slack_notification(queryset)
