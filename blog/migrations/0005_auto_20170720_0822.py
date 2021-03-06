# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-20 07:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170720_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 20, 7, 22, 14, 289506, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 20, 7, 22, 14, 288290, tzinfo=utc)),
        ),
    ]
