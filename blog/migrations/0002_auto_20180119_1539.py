# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 07:39
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
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 19, 7, 39, 26, 430000, tzinfo=utc)),
        ),
    ]
