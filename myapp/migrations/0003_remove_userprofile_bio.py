# Generated by Django 4.2.3 on 2023-10-07 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_userprofile_delete_command_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
    ]
