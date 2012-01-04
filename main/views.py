# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse
from main.models import UserProfile, Org
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms

def index(request):
    return render_to_response('main/index.html',
                              {},
                              context_instance=RequestContext(request))

def signup(request):
    return render_to_response('main/signup.html',
                              {},
                              context_instance=RequestContext(request))

def join(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST.get('first_name'),request.POST.get('email'),request.POST.get('password'))
        if user is not None:
            #request.session['user'] = uname
            return HttpResponseRedirect(reverse('main.views.dashboard'))

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
                              
def teams(request):
    return render_to_response('main/teams.html',
                              {},
                              context_instance=RequestContext(request))

def create_org(request):
    return render_to_response('main/new_team.html',
                              {'form':OrgForm()},
                              context_instance=RequestContext(request))


class OrgForm (forms.Form):
    choices = forms.ChoiceField(choices=Org.ORG_TYPES)

