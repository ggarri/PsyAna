from django.shortcuts import render
from django.shortcuts import render_to_response


def home(request):
    device = 'mobile' if request.is_mobile else 'web'
    return render_to_response(device+'/index.html')
