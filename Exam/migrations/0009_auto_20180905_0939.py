# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-05 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0008_auto_20180905_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondetail',
            name='person_img',
            field=models.ImageField(default=None, null=True, upload_to=b''),
        ),
    ]
