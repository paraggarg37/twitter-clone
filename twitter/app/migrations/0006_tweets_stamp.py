# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_tweets_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='stamp',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
