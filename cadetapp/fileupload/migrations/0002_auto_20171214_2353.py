# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='json_model',
            name='files',
            field=models.FilePathField(match='.*\\.csv$', path='/home/hartnerk/CADET_Sandbox/cadetapp/media/downloads/'),
        ),
    ]
