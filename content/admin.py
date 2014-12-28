from functools import update_wrapper
from django.contrib import admin
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from content.forms import SectionInlineFormSet
from content.models import Photo, Page, Section


class PhotoAdmin(admin.ModelAdmin):
    pass


# class SectionAdmin(admin.ModelAdmin):
#     pass


class SectionInline(admin.StackedInline):
    model = Section
    formset = SectionInlineFormSet
    template = "admin/stacked_inline_section.html"

    def __init__(self, *args, **kwargs):
        super(SectionInline, self).__init__(*args, **kwargs)
        self.extra = 0


class PageAdmin(admin.ModelAdmin):
    change_form_template = 'admin/change_form_page.html'
    preview__template = 'admin/preview__section.html'
    inlines = [
        SectionInline,
    ]

    def get_urls(self):
        from django.conf.urls import patterns, url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.model_name

        urls = patterns('',
            url(r'^(.+)/preview/$',
                wrap(self.preview_view),
                name='%s_%s_preview' % info),
        )

        super_urls = super(PageAdmin, self).get_urls()
        return urls + super_urls

    def preview_view(self, request, id, form_url='', extra_context=None):
        opts = Section._meta
        form = ManagePageForm()
        obj = Page.objects.get(pk=id)

        if not self.has_change_permission(request, obj):
            raise PermissionDenied

        # do cool management stuff here

        preserved_filters = self.get_preserved_filters(request)
        form_url = add_preserved_filters({'preserved_filters': preserved_filters, 'opts': opts}, form_url)

        context = {
            'title': 'Manage %s' % obj,
            'has_change_permission': self.has_change_permission(request, obj),
            'form_url': form_url,
            'opts': opts,
            'errors': form.errors,
            'app_label': opts.app_label,
            'original': obj,
        }

        context.update(extra_context or {})
        return render(request, self.preview__template, context)

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Page, PageAdmin)
# admin.site.register(Section, SectionAdmin)