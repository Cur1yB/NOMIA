# Generated by Django 4.2 on 2024-02-05 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0009_userresponse_global_question_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresponse',
            name='global_question_id',
        ),
    ]
