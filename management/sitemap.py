from django.contrib.sitemaps import Sitemap
from content.models import Page
from django.core.urlresolvers import reverse


class PageSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Page.objects.all()

    def location(self, item):
        return reverse(item.title)