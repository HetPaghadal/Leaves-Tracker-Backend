# Generated by Django 4.0.1 on 2022-01-19 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Created_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 19, 19, 48, 40, 573114), null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Updated_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 19, 19, 48, 40, 573145), null=True),
        ),
    ]