# Generated by Django 3.2.6 on 2021-09-23 04:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_employee_date_of_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_join',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 23, 10, 12, 9, 274506)),
        ),
    ]
