# Generated by Django 4.1.2 on 2022-10-09 19:09

import base.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', base.models.UserManager()),
            ],
        ),
    ]
