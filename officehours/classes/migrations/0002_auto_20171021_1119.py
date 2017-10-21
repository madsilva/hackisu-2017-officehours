# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-21 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='hawkid',
            new_name='canvas_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='current_session',
        ),
        migrations.AddField(
            model_name='question',
            name='status',
            field=models.CharField(choices=[('waiting', 'Waiting'), ('working', 'Working'), ('finished', 'Finished')], default='waiting', max_length=20),
        ),
        migrations.AddField(
            model_name='question',
            name='time_asked',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='password',
            field=models.CharField(default='', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='section',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('student', 'session')]),
        ),
    ]