from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils.timezone import datetime
from leavestracker.apps.employees.models import CustomUser

class Leaves(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_date = models.DateField(blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)
    reason = models.CharField(max_length = 30, null = True)

    def clean(self):
        if self.start_date>self.end_date:
            raise ValidationError('Invalid Date')
        if Leaves.objects.filter(Q(user_id=self.user) & Q(Q(Q(start_date__gte=self.start_date) & Q(start_date__lte=self.end_date)) | Q(Q(end_date__gte=self.start_date)& Q(end_date__lte=self.end_date)))).exists():
            raise ValidationError('Entry Exist')