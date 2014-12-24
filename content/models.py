from django.db import models
import os


class Photo(models.Model):
    image = models.ImageField(upload_to='Public/uploading')
    title = models.CharField(max_length=100, blank=True, default='NO TITLE')
    alt = models.CharField(max_length=255, blank=True, default='NO ALT')
    description = models.TextField(null=True)

    # def save(self, *args, **kwargs):
    #     if self.image[0] != '/':
    #         os.path.join('/', self.image)
    #     super(Photo, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.title
