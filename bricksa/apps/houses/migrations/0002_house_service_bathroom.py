# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-19 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='service_bathroom',
            field=models.IntegerField(default=0, verbose_name='Service Bathroom'),
        ),
    ]
