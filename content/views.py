from django.forms.models import modelformset_factory
from django.http.response import HttpResponseNotFound, HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from content.models import Page, Section, Website
from django.conf import settings
import subprocess
import commands


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


@csrf_exempt
def server_action(request):
    def handle_uploaded_file(f):
        with open(settings.PENDING_PSYANA_DUMPFILE, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    def run_command(exec_line):
        return commands.getoutput(exec_line)

    if not request.user.is_authenticated():
        return redirect('/admin/login/?next=%s' % request.path)
    if request.method != 'POST' or 'action' not in request.POST:
        return HttpResponse(content='Wrong Request Format', status=403)

    action = request.POST['action']

    if action == 'git_pull':
        cmd = 'cd %s && git pull origin master' % settings.BASE_DIR
    elif action == 'restart_nginx':
        cmd = '/etc/init.d/uwsgi_psyana restart 2>/var/log/uwsgi_psyana.log'
    elif action == 'apply_dump' and 'sql_dump_file' in request.FILES:
        handle_uploaded_file(request.FILES['sql_dump_file'])
        database_params = settings.DATABASES['default']
        cmd = 'mysql -u%s -p%s %s < %s' % (database_params['USER'], database_params['PASSWORD'],
                                           database_params['NAME'], settings.PENDING_PSYANA_DUMPFILE)
    else:
        return HttpResponse(content='Action selected not valid', status=403)

    output = run_command(cmd)
    if not output:
        output = 'Succesed'
    return HttpResponse(output)


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