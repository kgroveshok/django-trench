# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-13 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trench', '0002_auto_20190111_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mfamethod',
            name='secret',
            field=models.CharField(max_length=255, verbose_name='secret'),
        ),
        migrations.AlterField(
            model_name='mfamethod',
            name='_backup_codes',
            field=models.TextField(blank=True, verbose_name='backup codes'),
        ),
    ]
