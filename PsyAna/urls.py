from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from content.models import Page

import os
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'content.views.home', name='home'),
    url(r'^test$', 'content.views.test', name='test'),
    url(r'^render/section/(?P<section_id>\d+)?$', 'content.views.render_preview_section', name='render_preview_section'),
    url(r'^render/page/(?P<page_id>\d+)?$', 'content.views.render_preview_page', name='render_preview_page'),
    # url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls))
) + static(settings.STATIC_URL)

paths = Page.objects.values_list('path', flat=True)
for path in paths:
    url_path = path if path[0] != '/' else path[1:]
    if len(url_path) > 0:
        urlpatterns += url(r'^'+url_path+'$', 'content.views.render_page', {'page_id': path}),