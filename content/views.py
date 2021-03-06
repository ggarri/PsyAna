from django.forms.models import modelformset_factory
from django.http.response import HttpResponseNotFound
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from content.forms import SectionForm
from content.models import Page, Section, Website
from django.conf import settings


def home(request):
    page = Page.objects.get(path='/')
    if page is None:
        return HttpResponseNotFound('<h1>HomePage not found</h1><h2>Please, insert it via admin area</h2>')
    return render_page(request)


@csrf_exempt
def render_preview_section(request, section_id):
    device = 'mobile' if request.is_mobile else 'web'
    section = Section.objects.get(pk=section_id) if section_id != '0' else None
    if request.is_ajax():
        formset = SectionForm(request.POST)
        if formset.is_valid():
            sections = formset.save(commit=False)
            section = sections[0] if len(sections) > 0 else section

    return render_to_response('section/template/template_preview.html', {'section': section, 'isPreview': True, 'device': device},
                              context_instance=RequestContext(request))


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
    try:
        website = Website.objects.get(name=settings.WEBSITE_NAME)
    except Website.DoesNotExist:
        return HttpResponseNotFound('<h1>Website not found</h1><h2>Please, insert it via admin area</h2>')

    device = 'mobile' if request.is_mobile else 'web'
    office = website.office
    pages = Page.objects.filter(website__pk=website.pk).all()
    page = Page.objects.get(website__pk=website.pk, path=page_id)
    return render_to_response(page.get_html_template(),
                              {
                                  'website': website,
                                  'menus': pages.values('id', 'path', 'title'),
                                  'page': page,
                                  'device': device,
                                  'office': office
                              },
                              context_instance=RequestContext(request))