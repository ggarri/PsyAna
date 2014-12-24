from django.contrib import admin
from django.core.urlresolvers import reverse
from content.models import Photo
# from tinymce.widgets import TinyMCE


class PhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)