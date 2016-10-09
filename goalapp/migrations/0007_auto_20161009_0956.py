# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-09 07:56
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goalapp', '0006_goal_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='goal_funds',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=6),
        ),
        migrations.AlterField(
            model_name='goal',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goal', to='goalapp.User'),
        ),
    ]
