# Generated by Django 3.2.6 on 2021-09-21 07:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_projects_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_files',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='projects.projects'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='co_author',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('emp', 'emp'), ('bb', 'bb'), ('cc', 'cc'), ('aaaaaaaaaaaafd', 'aaaaaaaaaaaafd')], max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 12, 50, 10, 58279)),
        ),
    ]
