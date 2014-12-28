from django.forms.models import modelformset_factory, BaseInlineFormSet
from django.http.response import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from content.forms import SectionInlineFormSet
from management.models import Office
from content.models import Page, Section
from django.conf import settings


def home(request):
    page = Page.objects.get(path='/')
    if page is None:
        return HttpResponseNotFound('<h1>HomePage not found</h1><h2>Please, insert it via admin area</h2>')
    return render_page(request)

@csrf_exempt
def render_section(request, section_id):
    if request.is_ajax():
        section_form_set = modelformset_factory(Section)
        formset = section_form_set(request.POST)
        if formset.is_valid():
            sections = formset.save(commit=False)

    section = sections[0] if len(sections) > 0 else Section.objects.get(pk=section_id)
    html_template = section.get_html_template()
    return render_to_response(html_template, {'section': section},
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