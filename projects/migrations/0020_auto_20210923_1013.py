# Generated by Django 3.2.6 on 2021-09-23 04:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20210923_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_files',
            name='cover',
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 23, 10, 13, 23, 643867)),
        ),
    ]
