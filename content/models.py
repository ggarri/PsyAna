from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    birthday = models.DateField(default=None, blank=True, null=True)
    # description = tinymce_models.HTMLField()


class Photo(models.Model):
    image = models.ImageField()


class Office(models.Model):
    title = models.CharField(max_length=100, default='NO TITLE')
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    photos = models.ManyToManyField(Photo, blank=True)
    psicologies = models.ManyToManyField(UserProfile, blank=True)