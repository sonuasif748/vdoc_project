# Generated by Django 3.2.6 on 2021-09-29 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0046_auto_20210929_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 29, 12, 46, 16, 453579)),
        ),
    ]
