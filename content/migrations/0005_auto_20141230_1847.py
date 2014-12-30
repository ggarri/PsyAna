# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20141230_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='alt',
        ),
        migrations.AddField(
            model_name='section',
            name='info',
            field=models.CharField(max_length=170, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='keywords',
            field=models.ManyToManyField(to='content.Keyword', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='robot_tags',
            field=models.CharField(default=b'INDEX, FOLLOW', max_length=30, choices=[(b'noindex, follow', b'NOINDEX, FOLLOW'), (b'index, nofollow', b'INDEX, NOFOLLOW'), (b'noindex, nofollow', b'NOINDEX, NOFOLLOW'), (b'index, follow', b'INDEX, FOLLOW')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='website',
            name='keywords',
            field=models.ManyToManyField(to='content.Keyword', blank=True),
            preserve_default=True,
        ),
    ]
