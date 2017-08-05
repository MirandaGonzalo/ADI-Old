# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-27 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('dni', models.IntegerField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Formulario2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_alumno', models.CharField(max_length=20)),
                ('apellido_alumno', models.CharField(max_length=20)),
                ('dni_alumno', models.IntegerField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Padre_Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('dni', models.IntegerField()),
                ('email', models.EmailField(max_length=40)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Preceptor',
            fields=[
                ('nombre', models.CharField(max_length=20)),
                ('dni', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
