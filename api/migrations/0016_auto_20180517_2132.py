# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-17 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_lesson_homework'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Theme'),
        ),
    ]
