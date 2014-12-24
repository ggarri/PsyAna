from django.contrib import admin
from django.core.urlresolvers import reverse
from content.models import Photo, Page, Section
# from tinymce.widgets import TinyMCE


class PhotoAdmin(admin.ModelAdmin):
    pass


class PageAdmin(admin.ModelAdmin):
    pass


class SectionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Section, SectionAdmin)