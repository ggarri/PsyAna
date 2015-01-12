# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20150105_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='office',
            name='director',
            field=models.ForeignKey(related_name='director_of', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
