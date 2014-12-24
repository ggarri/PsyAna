from django.db import models
from content.models import Photo
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    birthday = models.DateField(default=None, blank=True, null=True)
    photos = models.ManyToManyField(Photo, blank=True, related_name='user_photos')
    profile_photo = models.OneToOneField(Photo, null=True, related_name='profile_photo')
    # description = tinymce_models.HTMLField()

    def __unicode__(self):
        return u'%s (%s %s)' % (self.username, self.first_name, self.last_name)


class Office(models.Model):
    title = models.CharField(max_length=100, default='NO TITLE')
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    photos = models.ManyToManyField(Photo, blank=True, related_name='office_photos')
    logo = models.OneToOneField(Photo, null=True, blank=True, related_name='office_logo')
    worker = models.ManyToManyField(UserProfile, blank=True, verbose_name="Psichology")

    def __unicode__(self):
        return u'%s' % self.title