# Generated by Django 3.2.6 on 2021-09-30 06:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0049_alter_employee_date_of_join'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='status',
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_join',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 11, 56, 27, 669104)),
        ),
    ]
