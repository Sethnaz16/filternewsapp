# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-22 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171115_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unreliablesource',
            name='label',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='unreliablesource',
            name='source',
            field=models.CharField(max_length=300),
        ),
    ]