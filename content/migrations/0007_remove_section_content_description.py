# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20141230_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='content_description',
        ),
    ]
