# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse
from main.models import UserProfile, Org
from django.contrib.auth import authenticate, login

def index(request):
    return render_to_response('main/index.html',
                              {},
                              context_instance=RequestContext(request))


def signin(request):
    if request.method == 'POST':
        uname = request.POST.get('user')
        pw = request.POST.get('password')
        #user = blah
        user = authenticate(username=uname, password=pw)
        if user is not None:
            #request.session['user'] = uname
            return HttpResponseRedirect(reverse('main.views.dashboard'))
                                  
def dashboard(request):
    return render_to_response('main/dashboard.html',
                              {},
                              context_instance=RequestContext(request))

def audits(request):
    return render_to_response('main/audits.html',
                              {},
                              context_instance=RequestContext(request))
                              
