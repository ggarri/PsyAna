# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
        ('content', '0003_auto_20141224_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(null=True, blank=True)),
                ('keywords', models.ManyToManyField(to='content.Keyword')),
                ('office', models.ForeignKey(to='management.Office')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='website',
            unique_together=set([('name',)]),
        ),
        migrations.AlterUniqueTogether(
            name='keyword',
            unique_together=set([('name',)]),
        ),
        migrations.AddField(
            model_name='page',
            name='alt',
            field=models.CharField(default=b'NO ALT', max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='keywords',
            field=models.ManyToManyField(to='content.Keyword'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='robot_tags',
            field=models.CharField(default=b'INDEX, FOLLOW', max_length=30, choices=[(b'NOINDEX, FOLLOW', b'NOINDEX, FOLLOW'), (b'INDEX, NOFOLLOW', b'INDEX, NOFOLLOW'), (b'NOINDEX, NOFOLLOW', b'NOINDEX, NOFOLLOW'), (b'INDEX, FOLLOW', b'INDEX, FOLLOW')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='website',
            field=models.ForeignKey(related_name='pages', to='content.Website', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='path',
            field=models.CharField(default=b'/', max_length=70),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.IntegerField(default=1, choices=[(1, b'base/base_simple.html'), (2, b'base/base_slider.html')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=70),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='alt',
            field=models.CharField(default=b'NO ALT', max_length=110, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(default=b'NO TITLE', max_length=70, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='subtitle',
            field=models.CharField(max_length=120, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(max_length=70, blank=True),
            preserve_default=True,
        ),
    ]
