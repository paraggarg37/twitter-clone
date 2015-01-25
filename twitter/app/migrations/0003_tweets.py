# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20150122_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('tid', models.AutoField(serialize=False, primary_key=True)),
                ('tweet', models.CharField(max_length=140, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
