# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-05 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('organization', models.CharField(max_length=70)),
                ('designation', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('country', models.CharField(max_length=25)),
            ],
        ),
    ]
