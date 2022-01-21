from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils.timezone import datetime
from leavestracker.apps.employees.models import CustomUser
from leavestracker.apps.leaves import constants as const

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
