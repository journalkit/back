# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-16 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20180516_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examlist',
            name='mark',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
