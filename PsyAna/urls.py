from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

import os
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'content.views.home', name='home'),
    # url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls))
) + static(settings.STATIC_URL)

sections = ('about', 'news', 'services', 'contact')
for section in sections:
    urlpatterns += url(r'^'+section+'$', 'content.views.section', {'sectionId': section}),