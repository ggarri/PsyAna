# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0005_alter_user_last_login_null'),
        ('content', '0012_auto_20150105_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='photos',
            field=models.ManyToManyField(related_name='website', to='content.Photo', blank=True),
            preserve_default=True,
        ),
    ]
