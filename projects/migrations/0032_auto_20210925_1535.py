# Generated by Django 3.2.6 on 2021-09-25 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0031_alter_projects_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 25, 15, 35, 11, 303364)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='work_progress',
            field=models.CharField(choices=[('0', '0%'), ('25', '25%'), ('50', '50%'), ('75', '75%'), ('100', '100%')], default=1, max_length=4),
        ),
    ]
