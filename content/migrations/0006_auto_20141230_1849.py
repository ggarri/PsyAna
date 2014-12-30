# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20141230_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='info',
            new_name='content_description',
        ),
    ]
