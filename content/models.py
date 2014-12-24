from django.db import models
import os


class Photo(models.Model):
    image = models.ImageField(upload_to='Public/uploading')
    title = models.CharField(max_length=100, blank=True, default='NO TITLE')
    alt = models.CharField(max_length=255, blank=True, default='NO ALT')
    description = models.TextField(null=True)

    def __unicode__(self):
        return u'%s' % self.title


class Page(models.Model):
    TEMPLATES = (
        (1, 'base/base.html'),
        (2, 'base/base_slider.html')
    )

    title = models.CharField(max_length=40)
    template = models.IntegerField(choices=TEMPLATES, default=1)
    path = models.CharField(max_length=40, blank=False, default='/')

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        unique_together = ( ('path'), )
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'


class Section(models.Model):
    SKELETON = (
        (1, 'section/section1_1.html'),
        (2, 'section/section1_2.html'),
        (3, 'section/section1_3.html'),
        (4, 'section/section2_3.html'),
    )

    TEMPLATES = (
        (1, 'section/template/template_title.html'),
        (2, 'section/template/template_title_image.html'),
        (3, 'section/template/template_title_subtitle.html'),
        (4, 'section/template/template_title_subtitle_image.html'),
    )

    page = models.ForeignKey(Page, related_name='sections')
    template = models.IntegerField(choices=TEMPLATES, default=1)
    skeleton = models.IntegerField(choices=SKELETON, default=1)
    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True)
    head_photo = models.ForeignKey(Photo, related_name='sections')

    def __unicode__(self):
        return u'%s - %s' % (self.page.title, self.title)

