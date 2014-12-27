from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
from content.models import Photo, Page, Section
# from tinymce.widgets import TinyMCE


class PhotoAdmin(admin.ModelAdmin):
    pass


# class SectionAdmin(admin.ModelAdmin):
#     pass


class SectionInline(admin.StackedInline):
    model = Section

    def __init__(self, *args, **kwargs):
        super(SectionInline, self).__init__(*args, **kwargs)
        self.extra = 0


class PageAdmin(admin.ModelAdmin):
    inlines = [
        SectionInline,
    ]

    @staticmethod
    def get_extra(self, request, obj=None, **kwargs):
        return 0

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Page, PageAdmin)
# admin.site.register(Section, SectionAdmin)