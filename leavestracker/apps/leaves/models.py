from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.db.models import Q
from django.utils.timezone import datetime
from leavestracker.apps.employees.models import CustomUser
from leavestracker.apps.leaves import constants as const

import datetime
import json
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
    def get_today_leaves(self):
        today = datetime.date.today()

        queryset = self.objects.filter(
            start_date__lte=today, end_date__gte=today
        )
        return queryset

    @classmethod
    def create_message(self, Data):
        message = 'Today Leaves :'
        for x in Data:
            message = message + '\n'
            message = message + str(x.user.first_name) + ' ' + str(x.user.last_name)+ ' (Reason:' + str(x.reason) + ')'

        payload = {
            "text": message
        }

        url = 'https://hooks.slack.com/services/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'
        response = requests.post(url, data=json.dumps(payload))

    @classmethod
    def send_notification(self):
        queryset = self.get_today_leaves()
        self.create_message(queryset)
