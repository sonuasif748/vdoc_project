# Generated by Django 3.2.6 on 2021-09-29 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0039_auto_20210929_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_join',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 29, 12, 23, 39, 101505)),
        ),
    ]
