from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail
from content.models import Website
from django.conf import settings
import subprocess
import commands
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
import xml.etree.cElementTree as ET
# Create your views here.


def certificate(request, certificate_id):
    return render(request, 'googleStuff/google'+certificate_id+'.html')


def sitemap(request):
    response = HttpResponse(content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename="sitemap.xml"'

    root = ET.Element("root")
    doc = ET.SubElement(root, "doc")
    ET.SubElement(doc, "field1", name="blah").text = "some value1"
    ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

    return render(request, ET.tostringlist(root), {}, content_type="text/xml")


@csrf_exempt
def client_contact_form(request):
    body_data = json.loads(request.body)
    website = Website.objects.get(name=settings.WEBSITE_NAME)
    recipients = [website.office.director.email]
    # recipients = ['ggarri@gmail.com']

    send_mail('PsyAna : %s' % body_data['fullname'], body_data['comment'], body_data['email'], recipients)
    return HttpResponse()


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
        cmd = 'cd %s && git reset --hard HEAD && git pull origin master' % settings.BASE_DIR
    elif action == 'restart_nginx':
        cmd = '/etc/init.d/uwsgi_psyana restart'
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