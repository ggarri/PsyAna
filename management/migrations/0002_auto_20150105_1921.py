# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
        (b'auth', b'__first__'),
        (b'contenttypes', b'__first__'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='address',
        ),
        migrations.RemoveField(
            model_name='office',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='office',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='office',
            name='worker',
        ),
        migrations.AddField(
            model_name='office',
            name='director',
            field=models.ForeignKey(related_name='director_of', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='office',
            name='workers',
            field=models.ManyToManyField(related_name='offices', verbose_name=b'Psichology', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.OneToOneField(related_name='profile_photo', null=True, blank=True, to='content.Photo'),
            preserve_default=True,
        ),
    ]
