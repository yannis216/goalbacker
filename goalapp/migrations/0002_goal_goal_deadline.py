# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goalapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='goal_deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
