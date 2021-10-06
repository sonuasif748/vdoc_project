# Generated by Django 3.2.6 on 2021-10-06 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0061_alter_employee_date_of_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_join',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 6, 15, 39, 50, 323858)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='Users/Profile_pictures'),
        ),
    ]