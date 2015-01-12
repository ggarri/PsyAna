# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_website_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='template',
            field=models.IntegerField(default=1, choices=[(1, b'section/template/template_title.html'), (2, b'section/template/template_title_image.html'), (3, b'section/template/template_title_subtitle.html'), (4, b'section/template/template_title_subtitle_image.html'), (5, b'section/template/contact.html'), (6, b'section/template/who_we_are.html')]),
            preserve_default=True,
        ),
    ]
