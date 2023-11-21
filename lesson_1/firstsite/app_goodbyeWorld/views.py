from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def goodbyeWorld(request, *args, **kwargs):
    return HttpResponse(f'Goodbye world!')