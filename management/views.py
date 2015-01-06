from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail
from content.models import Website
from django.conf import settings


# Create your views here.


@csrf_exempt
def client_contact_form(request):
    body_data = json.loads(request.body)
    website = Website.objects.get(name=settings.WEBSITE_NAME)
    recipients = [website.office.director.email]
    recipients = ['ggarri@gmail.com']

    send_mail('PsyAna : %s' % body_data['fullname'], body_data['request'], body_data['email'], recipients)
    return HttpResponse()