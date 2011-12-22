# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse


def index(request):
    return render_to_response('main/index.html',
                              {},
                              context_instance=RequestContext(request))


def signin(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        request.session['user'] = user
        return HttpResponseRedirect(reverse('main.views.dashboard'))
                                  
def dashboard(request):
    print request.session['user']
    return render_to_response('main/dashboard.html',
                              {},
                              context_instance=RequestContext(request))
