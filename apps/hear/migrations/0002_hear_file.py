# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hear', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hear',
            name='file',
            field=models.FileField(default='null.mp3', upload_to='hear'),
        ),
    ]
