# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 11:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170726_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 26, 11, 41, 38, 459220, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 26, 11, 41, 38, 457984, tzinfo=utc)),
        ),
    ]