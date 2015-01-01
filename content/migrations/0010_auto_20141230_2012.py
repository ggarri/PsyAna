# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_section_css_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='css_class',
        ),
        migrations.AddField(
            model_name='page',
            name='css_class',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
