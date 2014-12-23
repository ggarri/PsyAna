from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from content.models import Office, UserProfile


def home(request):
    device = 'mobile' if request.is_mobile else 'web'
    office = Office.objects.get(pk=1)
    return render_to_response(device+'/home.html',
                              {
                                  'device': device,
                                  'office': office
                              }, context_instance=RequestContext(request))
