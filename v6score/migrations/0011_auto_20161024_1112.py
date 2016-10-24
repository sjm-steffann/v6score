# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 11:12
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v6score', '0010_auto_20161024_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='ping6_1500_latencies',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='measurement',
            name='ping6_latencies',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, default=list, size=None),
        ),
    ]
