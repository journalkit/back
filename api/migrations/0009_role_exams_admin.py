# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-11 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20180509_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='exams_admin',
            field=models.BooleanField(default=False),
        ),
    ]
