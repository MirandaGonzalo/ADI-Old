# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-31 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adi', '0004_formulario3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='id',
        ),
        migrations.AlterField(
            model_name='alumno',
            name='dni',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]