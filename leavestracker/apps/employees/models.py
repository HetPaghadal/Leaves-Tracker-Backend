from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import datetime


class CustomUser(AbstractUser):
    Created_date = models.DateField(blank=True, null=True)
    Updated_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email

    # id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active,
    # date_joined, Created_date, Updated_date