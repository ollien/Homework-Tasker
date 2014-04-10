from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from models import Session
from models import Homework
from models import Subject
def index(request):
	c=RequestContext(request)
	sessionQuery=request.COOKIES.get('sessionId')
	if sessionQuery!=None:
		query=Session.objects.filter(sessionId=sessionQuery)
		if len(query)==1:
			return listView(request,query[0].userId)
	return render_to_response('index.html',{},c)	
def register(request):
	c=RequestContext(request)
	return render_to_response('register.html',{},c)
def listView(request,user):
	c=RequestContext(request)
	homeworkQuery=Homework.objects.filter(userId=user).order_by('priority')
	subjectQuery=Subject.objects.filter(userId=user)
	# assignments={}
	# for index,item in zip(range(len(query)),query):
	# 	assignments[index]=item
	return render_to_response('list.html',{'assignments':homeworkQuery,'subjects':subjectQuery},c)
	#return HttpResponse("Should have redirected! Welcome "+user.user)