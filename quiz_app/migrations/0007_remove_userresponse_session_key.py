# Generated by Django 4.2 on 2024-02-05 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0006_userresponse_session_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresponse',
            name='session_key',
        ),
    ]
