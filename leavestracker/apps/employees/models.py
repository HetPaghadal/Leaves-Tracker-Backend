from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import datetime


class CustomUser(AbstractUser):
    created_date = models.DateField(blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email
