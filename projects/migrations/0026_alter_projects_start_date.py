# Generated by Django 3.2.6 on 2021-09-24 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_alter_projects_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 24, 13, 55, 0, 180981)),
        ),
    ]
