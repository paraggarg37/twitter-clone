# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150123_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 24, 13, 44, 6, 103468, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
