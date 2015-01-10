# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import content.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_section_css_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.IntegerField(default=1, choices=[(1, b'base/base_simple.html'), (2, b'base/base_slider.html'), (3, b'base/base_maps.html')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='alt',
            field=models.CharField(max_length=110, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(storage=content.models.MyStorage(base_url=b'/Public/uploading', location=b'/home/ggarrido/projects/PsyAna/Public/uploading'), upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=70),
            preserve_default=True,
        ),
    ]
