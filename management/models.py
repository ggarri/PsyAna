from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    birthday = models.DateField(default=None, blank=True, null=True)
    profile_photo = models.OneToOneField('content.Photo', null=True, blank=True, related_name='profile_photo')
    description = models.TextField(blank=True, default='')

    def __unicode__(self):
        return u'%s (%s %s)' % (self.username, self.first_name, self.last_name)


class Office(models.Model):
    title = models.CharField(max_length=100, default='NO TITLE')
    logo = models.OneToOneField('content.Photo', null=True, blank=True, related_name='office_logo')
    workers = models.ManyToManyField(UserProfile, blank=True, verbose_name="Psichology", related_name='offices')
    director = models.ForeignKey(UserProfile, null=False, related_name='director_of')

    def __unicode__(self):
        return u'%s' % self.title