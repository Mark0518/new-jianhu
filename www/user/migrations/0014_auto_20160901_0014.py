# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-01 00:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_myrecommend_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myrecommend',
            name='uuid',
            field=models.CharField(db_index=True, max_length=36),
        ),
    ]