from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

def index(request):
	c=RequestContext(request)
	return render_to_response('index.html',{},c)
def register(request):
	c=RequestContext(request)
	return render_to_response('register.html',{},c)