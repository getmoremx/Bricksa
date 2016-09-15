# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-14 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20160907_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='google_maps_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='video',
            field=models.URLField(blank=True, null=True, verbose_name='Video'),
        ),
    ]
