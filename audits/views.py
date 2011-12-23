# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse

def create_audit(request):
    return render_to_response('audits/new_audit.html',
                              {},
                              context_instance=RequestContext(request))
