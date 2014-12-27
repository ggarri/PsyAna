from django.http.response import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from management.models import Office
from content.models import Page
from django.conf import settings


def home(request):
    page = Page.objects.get(path='/')
    if page is None:
        return HttpResponseNotFound('<h1>HomePage not found</h1><h2>Please, insert it via admin area</h2>')
    return render_page(request)
    redirect_url = reverse('content.views.render_page')
    return HttpResponseRedirect(reverse('content.views.render_page'))


def test(request):
    device = 'mobile' if request.is_mobile else 'web'
    return render_to_response('web/news.html',
                              {
                                  'menus': Page.objects.values('id', 'path', 'title'),
                                  'device': device,
                                  'menu_selected': 0
                              },
                              context_instance=RequestContext(request))


def render_page(request, page_id='/'):
    device = 'mobile' if request.is_mobile else 'web'
    offices = Office.objects.filter(title=settings.OFFICE_NAME)
    office = offices[0] if len(offices) > 0 else None
    if office is None:
        return HttpResponseNotFound('<h1>Office not found</h1><h2>Please, insert it via admin area</h2>')

    page = Page.objects.get(path=page_id)
    sections = page.sections.all()
    html_template = page.get_html_template()
    return render_to_response(html_template,
                              {
                                  'menus': Page.objects.values('id', 'path', 'title'),
                                  'menu_selected': page.id,
                                  'sections': sections,
                                  'device': device,
                                  'office': office
                              },
                              context_instance=RequestContext(request))