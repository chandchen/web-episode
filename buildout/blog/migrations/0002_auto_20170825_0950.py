# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 09:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 25, 9, 50, 58, 106588, tzinfo=utc)),
        ),
    ]