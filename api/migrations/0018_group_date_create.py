# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-27 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20180526_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='date_create',
            field=models.DateField(default='2014-09-01'),
            preserve_default=False,
        ),
    ]
