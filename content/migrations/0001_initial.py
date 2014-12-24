# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'Public/uploading')),
                ('title', models.CharField(default=b'NO TITLE', max_length=100, blank=True)),
                ('alt', models.CharField(default=b'NO ALT', max_length=255, blank=True)),
                ('description', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        )
    ]
