# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-31 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20160831_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail_1',
            field=models.ImageField(default='file', upload_to=b'project_photos', verbose_name='Thumbnail 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='thumbnail_2',
            field=models.ImageField(default='file', upload_to=b'project_photos', verbose_name='Thumbnail 2'),
            preserve_default=False,
        ),
    ]
