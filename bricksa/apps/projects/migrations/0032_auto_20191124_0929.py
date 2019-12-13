# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-11-24 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0031_socialnetworks'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='car_ramp',
            field=models.BooleanField(default=False, verbose_name='Car Ramp'),
        ),
        migrations.AddField(
            model_name='project',
            name='extra_1',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Extra 1'),
        ),
        migrations.AddField(
            model_name='project',
            name='extra_2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Extra 2'),
        ),
        migrations.AddField(
            model_name='project',
            name='extra_3',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Extra 3'),
        ),
        migrations.AddField(
            model_name='project',
            name='indoor_garden',
            field=models.BooleanField(default=False, verbose_name='Indoor Garden'),
        ),
        migrations.AddField(
            model_name='project',
            name='solar_panel',
            field=models.BooleanField(default=False, verbose_name='Solar Panel'),
        ),
        migrations.AddField(
            model_name='project',
            name='warehouse',
            field=models.BooleanField(default=False, verbose_name='Warehouse'),
        ),
        migrations.AddField(
            model_name='project',
            name='water_treatment_plant',
            field=models.BooleanField(default=False, verbose_name='Water Treatment Plant'),
        ),
    ]