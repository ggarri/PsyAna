from django.db import models
from django.utils.encoding import filepath_to_uri
from management.models import Office
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


class MyStorage(FileSystemStorage):

        def url(self, name):
            if self.base_url is None:
                raise ValueError("This file is not accessible via a URL.")
            return os.path.join(self.base_url, filepath_to_uri(name))

fs = MyStorage(location=settings.CUSTOM_STORAGE_FOLDER_ROOT, base_url=settings.CUSTOM_STORAGE_FOLDER)


class Photo(models.Model):
    image = models.ImageField(storage=fs)
    title = models.CharField(max_length=70, blank=False)
    alt = models.CharField(max_length=110, blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Photo, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            try:
                this = Photo.objects.get(id=self.id)
                if this.image != self.image:
                    this.image.delete(save=False)
            except OSError as e:
                # when new photo then we do nothing, normal case
                pass

        super(Photo, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.title


class Keyword(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        unique_together = ( ('name'), )


class Website(models.Model):
    name = models.CharField(max_length=100, blank=False)
    url = models.CharField(max_length=250)
    office = models.ForeignKey(Office)
    photos = models.ManyToManyField(Photo, blank=True, related_name='website')
    title = models.CharField(max_length=70, blank=False)
    description = models.TextField(null=True, blank=True)
    # Max 20 Keywords under
    keywords = models.ManyToManyField(Keyword, blank=True)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        unique_together = ( ('name'), )


class Page(models.Model):
    TEMPLATES = (
        (1, 'base/base_simple.html'),
        (2, 'base/base_slider.html'),
        (3, 'base/base_maps.html'),
    )

    ROBOT_TAGS = (
        ('noindex, follow', 'NOINDEX, FOLLOW'),
        ('index, nofollow', 'INDEX, NOFOLLOW'),
        ('noindex, nofollow', 'NOINDEX, NOFOLLOW'),
        ('index, follow', 'INDEX, FOLLOW')
    )

    title = models.CharField(max_length=70)
    template = models.IntegerField(choices=TEMPLATES, default=1)
    path = models.CharField(max_length=70, blank=False, default='/')
    keywords = models.ManyToManyField(Keyword, blank=True)
    description = models.TextField(null=True, blank=True)
    css_class = models.CharField(max_length=100, blank=True, null=True)
    robot_tags = models.CharField(max_length=30, choices=ROBOT_TAGS, default='INDEX, FOLLOW')
    website = models.ForeignKey(Website, related_name='pages', null=True)

    @staticmethod
    def convert_template_id(template_id):
        return [y[1] for x, y in enumerate(Page.TEMPLATES) if y[0] == template_id][0]

    def get_html_template(self):
        return Page.convert_template_id(self.template)

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
        (5, 'section/template/contact.html'),
        (6, 'section/template/who_we_are.html'),
        (7, 'section/template/template_title_content_image.html'),
    )

    page = models.ForeignKey(Page, related_name='sections')
    template = models.IntegerField(choices=TEMPLATES, default=1)
    skeleton = models.IntegerField(choices=SKELETON, default=1)
    title = models.CharField(max_length=70, blank=True)
    subtitle = models.CharField(max_length=120, blank=True, null=True)
    text = models.TextField(blank=True)
    head_photo = models.ForeignKey(Photo, related_name='sections', blank=True, null=True)
    css_class = models.CharField(max_length=100, blank=True, null=True)

    @staticmethod
    def convert_template_id(template_id):
        return [y[1] for x, y in enumerate(Section.TEMPLATES) if y[0] == template_id][0]

    def get_html_template(self):
        return Section.convert_template_id(self.template)

    @staticmethod
    def convert_skeleton_id(skeleton_id):
        return [y[1] for x, y in enumerate(Section.SKELETON) if y[0] == skeleton_id][0]

    def get_html_skeleton(self):
        return Section.convert_skeleton_id(self.skeleton)

    def __unicode__(self):
        return u'%s - %s' % (self.page.title, self.title)

