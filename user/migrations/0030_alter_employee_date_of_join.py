# Generated by Django 3.2.6 on 2021-09-25 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_alter_employee_date_of_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_join',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 25, 15, 33, 47, 365681)),
        ),
    ]
