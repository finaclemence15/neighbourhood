# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-05 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0002_auto_20191105_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]