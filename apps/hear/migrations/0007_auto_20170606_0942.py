# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hear', '0006_auto_20170606_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hear',
            name='artist',
            field=models.CharField(db_column='artist', default=0, max_length=255),
        ),
    ]