# Generated by Django 3.2.6 on 2021-09-22 10:26

import datetime
from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_alter_projects_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='images',
            field=models.ImageField(blank='True', null='True', upload_to=projects.models.upload_location1),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 22, 15, 56, 51, 837636)),
        ),
    ]
