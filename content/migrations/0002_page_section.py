# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('template', models.IntegerField(default=1, choices=[(1, b'base/base.html'), (2, b'base/base_slider.html')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template', models.IntegerField(default=1, choices=[(1, b'section/template/template_title.html'), (2, b'section/template/template_title_image.html'), (3, b'section/template/template_title_subtitle.html'), (4, b'section/template/template_title_subtitle_image.html')])),
                ('skeleton', models.IntegerField(default=1, choices=[(1, b'section/section1_1.html'), (2, b'section/section1_2.html'), (3, b'section/section1_3.html'), (4, b'section/section2_3.html')])),
                ('title', models.CharField(max_length=100, blank=True)),
                ('subtitle', models.CharField(max_length=200, null=True, blank=True)),
                ('text', models.TextField(blank=True)),
                ('head_photo', models.ForeignKey(related_name='sections', to='content.Photo')),
                ('page', models.ForeignKey(related_name='sections', to='content.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
