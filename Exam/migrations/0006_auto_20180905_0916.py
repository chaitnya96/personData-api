# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-05 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0005_auto_20180905_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondetail',
            name='First_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='persondetail',
            name='Last_name',
            field=models.CharField(max_length=250),
        ),
    ]