# Generated by Django 5.1.4 on 2024-12-08 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_remove_tasks_status_members_confpassword_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='confpassword',
        ),
    ]
