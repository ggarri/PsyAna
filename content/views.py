from django.shortcuts import render_to_response
from django.template.context import RequestContext
from management.models import Office, UserProfile
from django.conf import settings


def home(request):
    device = 'mobile' if request.is_mobile else 'web'
    offices = Office.objects.filter(title=settings.OFFICE_NAME)
    office = offices[0] if len(offices) > 0 else None

    return render_to_response(device+'/home.html',
                              {
                                  'device': device,
                                  'office': office
                              }, context_instance=RequestContext(request))
