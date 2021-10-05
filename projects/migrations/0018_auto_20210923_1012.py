# Generated by Django 3.2.6 on 2021-09-23 04:42

import datetime
from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20210922_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_images', models.ImageField(blank='True', null='True', upload_to=projects.models.upload_location)),
            ],
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 23, 10, 12, 9, 274506)),
        ),
    ]