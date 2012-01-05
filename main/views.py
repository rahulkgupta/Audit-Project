# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse
from main.models import UserProfile, Org, Membership
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
        user = User.objects.create_user(request.POST.get('email'),request.POST.get('email'),request.POST.get('password'))
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user_profile = UserProfile (user=user)
        user_profile.save()
        if user is not None:
            request.session['user'] = user_profile
            return HttpResponseRedirect(reverse('main.views.dashboard'))

def signin(request):
    if request.method == 'POST':
        uname = request.POST.get('user')
        pw = request.POST.get('password')
        user = authenticate(username=uname, password=pw)
        print user
        #user_profile = UserProfile.objects.filter(user=user)
        if user is not None:
            #request.session['user'] = user_profile
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
    if request.method == 'POST':
        form = OrgForm(request.POST)
        if form.is_valid():
            user = request.session['user']
            name = form.cleaned_data['name']
            choice = form.cleaned_data['choices']
            parent = form.cleaned_data['parent_choices']
            if parent is None:
                org = Org(name=name,creator=user,org_type=choice, accepted=True)
            else:
                org = Org(name=name,creator=user,org_type=choice, accepted=False,parent=parent)
            org.save()
            member = Membership(user=user,org=org,accepted=True)
            member.save()
            return HttpResponseRedirect(reverse('main.views.dashboard'))
    else:
        return render_to_response('main/new_team.html',
                              {'form':OrgForm()},
                              context_instance=RequestContext(request))

def join_org(request):
    user = request.session['user']
    if request.method == 'POST':
        ""
    else:
        return render_to_response('main/join_team.html',
                              {'form':MemberForm(user)},
                              context_instance=RequestContext(request))

class OrgForm (forms.Form):
    name = forms.CharField(max_length=100)
    choices = forms.ChoiceField(choices=Org.ORG_TYPES)
    parent_choices = forms.ModelChoiceField(queryset=Org.objects.all())

class MemberForm (forms.Form):

    def __init__ (self, user, *args, **kwargs):
        super(MemberForm,self).__init__(*args, **kwargs)
        self.fields['choices'] = forms.ModelChoiceField(queryset=Org.objects.filter(members__user=user))
