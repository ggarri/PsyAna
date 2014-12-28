from MySQLdb.constants.ER import NO
from django.forms.models import modelformset_factory, BaseInlineFormSet, inlineformset_factory
from django.http.response import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from content.forms import SectionInlineFormSet, PageFormSet
from management.models import Office
from content.models import Page, Section
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
        section_form_set = modelformset_factory(Section)
        formset = section_form_set(request.POST)
        if formset.is_valid():
            sections = formset.save(commit=False)
            section = sections[0] if len(sections) > 0 else section

    return render_to_response('section/template/template_preview.html', {'section': section, 'isPreview': True, 'device': device},
                              context_instance=RequestContext(request))


@csrf_exempt
def render_preview_page(request, page_id):
    device = 'mobile' if request.is_mobile else 'web'
    page = Page.objects.get(pk=page_id) if page_id != '0' else None
    if request.is_ajax():
        page_form_set = modelformset_factory(Page)
        formset = page_form_set(request.POST)
        if formset.is_valid():
            pages = formset.save(commit=False)
            page = pages[0] if len(pages) > 0 else page

    return render_to_response('base/template_preview.html', {
        'sections': page.sections.all(),
        'device': device
    }, context_instance=RequestContext(request))


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