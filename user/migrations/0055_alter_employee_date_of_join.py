# Generated by Django 3.2.6 on 2021-10-05 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0054_alter_employee_date_of_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_join',
            field=models.DateTimeField(),
        ),
    ]
