from django.contrib import admin
from content.forms import SectionInlineFormSet, PageFormSet
from content.models import Photo, Page, Section, Website, Keyword


class KeywordSiteInline(admin.StackedInline):
    model = Website.keywords.through

    def __init__(self, *args, **kwargs):
        super(KeywordSiteInline, self).__init__(*args, **kwargs)
        self.extra = 0


class KeywordPageInline(admin.StackedInline):
    model = Page.keywords.through

    def __init__(self, *args, **kwargs):
        super(KeywordPageInline, self).__init__(*args, **kwargs)
        self.extra = 0


class KeywordAdmin(admin.ModelAdmin):
    pass


class PhotoAdmin(admin.ModelAdmin):
    change_form_template = 'admin/model_admin_photo.html'
    pass


class WebsiteAdmin(admin.ModelAdmin):
    inlines = [
        KeywordSiteInline,
    ]
    exclude = ('keywords', )


class SectionInline(admin.StackedInline):
    model = Section
    formset = SectionInlineFormSet
    template = "admin/stacked_inline_section.html"

    def __init__(self, *args, **kwargs):
        super(SectionInline, self).__init__(*args, **kwargs)
        self.extra = 0


class PageAdmin(admin.ModelAdmin):
    change_form_template = 'admin/model_admin_page.html'
    formset = PageFormSet
    inlines = [
        KeywordPageInline,
        SectionInline,
    ]
    exclude = ('sections', 'keywords')


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Keyword, KeywordAdmin)
