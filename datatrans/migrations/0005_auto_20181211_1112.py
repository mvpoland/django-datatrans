# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-12-11 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datatrans', '0004_auto_20181126_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyvalue',
            name='language',
            field=models.CharField(choices=[('en-pl', 'English (Poland)'), ('pl-pl', 'Polish')], db_index=True, max_length=5),
        ),
    ]
