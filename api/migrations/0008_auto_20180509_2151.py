# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-09 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180509_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
