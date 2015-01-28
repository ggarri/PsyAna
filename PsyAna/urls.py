from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from content.models import Page
from django.contrib.sitemaps.views import sitemap
from management.sitemap import PageSitemap

admin.site.index_template = 'admin/my_custom_index.html'
admin.autodiscover()

sitemaps = {
    'static': PageSitemap,
}


urlpatterns = patterns('',
    url(r'^google(?P<certificate_id>\w+)\.html$', 'management.views.certificate', name='certificate'),
    url(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    url(r'^management/client/contactform?$', 'management.views.client_contact_form', name='client_contact_form'),

    url(r'^admin/server-action', 'management.views.server_action', name='server_action'),
    url(r'^render/section/(?P<section_id>\d+)?$', 'content.views.render_preview_section', name='render_preview_section'),
    url(r'^admin/', include(admin.site.urls))
) + static(settings.STATIC_URL)

pages = Page.objects.all()
for page in pages:
    url_path = page.path if page.path[0] != '/' else page.path[1:]
    urlpatterns += url(r'^'+url_path+'$', 'content.views.render_page', {'page_id': page.path}, name=page.title),