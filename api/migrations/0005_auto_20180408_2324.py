# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-08 18:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180402_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('closed', models.BooleanField()),
                ('discipline', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Discipline')),
            ],
        ),
        migrations.CreateModel(
            name='ExamList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=256, null=True)),
                ('mark', models.CharField(default='н', max_length=1)),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('control1', models.CharField(max_length=256, null=True)),
                ('control2', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark1', models.CharField(default='*', max_length=1)),
                ('mark2', models.CharField(default='*', max_length=1)),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_open', models.DateField()),
                ('date_close', models.DateField(null=True)),
                ('discipline', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Discipline')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
                ('surname', models.CharField(max_length=256, null=True)),
                ('patronymic', models.CharField(max_length=256, null=True)),
                ('record_book', models.CharField(max_length=256, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('discipline', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Discipline')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.Role'),
        ),
        migrations.AddField(
            model_name='record',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Student'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='statement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Statement'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Theme'),
        ),
        migrations.AddField(
            model_name='examlist',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Student'),
        ),
        migrations.AddField(
            model_name='exam',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Group'),
        ),
        migrations.AddField(
            model_name='discipline',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.User'),
        ),
    ]
