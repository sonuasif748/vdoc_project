# Generated by Django 3.2.6 on 2021-09-22 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20210922_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='images',
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 22, 13, 37, 36, 490590)),
        ),
    ]
