# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-16 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_auto_20180712_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='courseDuration',
            field=models.CharField(default=4, max_length=120),
            preserve_default=False,
        ),
    ]
