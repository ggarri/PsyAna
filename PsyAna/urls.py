from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from content.models import Page

import os

admin.site.index_template = 'admin/my_custom_index.html'
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'content.views.home', name='home'),
    url(r'^googlefbb7059c456c58a6\.html$', 'management.views.certificate', name='certificate'),
    url(r'^management/client/contactform?$', 'management.views.client_contact_form', name='client_contact_form'),

    url(r'^admin/server-action', 'management.views.server_action', name='server_action'),
    url(r'^render/section/(?P<section_id>\d+)?$', 'content.views.render_preview_section', name='render_preview_section'),
    url(r'^admin/', include(admin.site.urls))
) + static(settings.STATIC_URL)

paths = Page.objects.values_list('path', flat=True)
for path in paths:
    url_path = path if path[0] != '/' else path[1:]
    if len(url_path) > 0:
        urlpatterns += url(r'^'+url_path+'$', 'content.views.render_page', {'page_id': path}),