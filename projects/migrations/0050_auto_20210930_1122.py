# Generated by Django 3.2.6 on 2021-09-30 05:52

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0049_auto_20210929_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='co_author',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('ff', 'ff'), ('pp', 'pp'), ('ttt', 'ttt')], max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 11, 22, 53, 772913)),
        ),
    ]
