# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 20:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='CourseModeOfDelivery',
            new_name='courseModeOfDelivery',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='CoursePrerequisite',
            new_name='coursePrerequisite',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='CourseSkillLevel',
            new_name='courseSkillLevel',
        ),
    ]
