# Generated by Django 3.2.6 on 2021-09-23 04:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20210923_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_images',
            name='project_img',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projects'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 23, 10, 12, 22, 986390)),
        ),
    ]
