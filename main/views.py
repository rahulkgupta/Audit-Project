# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader

def index(request):
    return render_to_response('main/index.html',{})
