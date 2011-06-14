from django.shortcuts import render_to_response
from thesite.models import pages
from django.http import HttpResponse

def index(request):
    current_pages = pages.objects.all()
    return render_to_response('thesite/index.html', {'pages' : current_pages})

def info(request):
    current_pages = pages.objects.all()
    return render_to_response('thesite/index.html', {'pages' : current_pages})

def experiments(request):
    current_pages = pages.objects.all()
    return render_to_response('thesite/index.html', {'pages' : current_pages})
