# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-17 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adi', '0016_auto_20170815_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario2',
            name='estado',
            field=models.CharField(default=4, max_length=8),
            preserve_default=False,
        ),
    ]