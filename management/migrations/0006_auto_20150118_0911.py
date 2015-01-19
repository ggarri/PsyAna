# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_remove_userprofile_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='sn_facebook',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sn_google',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
    ]
