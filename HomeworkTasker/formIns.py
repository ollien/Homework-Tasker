from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.shortcuts import redirect
import json
#this is needed for hashes and salts :D
import hashlib
import uuid

import re

#Here we're just gonna import the models as needed, rather than a messy * import
from models import User
from models import Session
from models import Homework
from models import Subject

import userHandling
import datetime

def loginForm(request):
	c=RequestContext(request)
	if request.method=='POST':
		# query=User.objects.filter(user=user)
		# result={}
		# if len(query)==0:
		# 	query=User.objects.filter(email=user)
		# 	if len(query)==0:
		# 		result['result']='userDoesNotExist'
		# if len(query)==1:
		# 	usersPassword=query[0].password
		# 	usersSalt=query[0].salt
		# 	if (hashlib.sha512(password+usersSalt).hexdigest()==usersPassword):
		# 		result['result']='OK'
		# 	else:
		# 		result['result']='invalidCredentials'
		# elif len(query)>1:
		# 	result['result']='somethingWentHorriblyWrong'
		user=request.POST.get('username')
		password=request.POST.get('password')
		persist=True if request.POST.get('persist')=='true' else False
		result=userHandling.login(user,password,persist) #Change this from false
		response=HttpResponse(json.dumps(result))
		if (result['result']=='OK'):
			exp=None
			if persist:
				exp=datetime.date.today()+datetime.timedelta(14,0)
			print 'Expires:',
			print exp
			response.set_cookie('sessionId',result['sessionId'],path='/',expires=exp)
		return response
# def sessionLogin(request):
#     c=RequestContext(request)
#     result={}
#     try:
#         query=Session.objects.filter(sessionId=reqeust.POST.get('sessionId'))
#         if len(query)==1:
#             
#         elif len(query)==0:
#             #Do Nothing
#             print 'nothing'
#             result['result']='noSessionExists'
#         elif len(query)>2:
#             #Horribly wrong
#             print 'something went horribly wrong'
#             result['result']='somethingWentHorriblyWrong'
#     except:
#         result['result']='somethingWentHorriblyWrong'
#         return HttpResponse(json.dumps(result))
		
def loginSuccess(request):
	return redirect("/")
def registerForm(request):
	c=RequestContext(request)
	result={'result':[]}
	if request.method=='POST':
		user=request.POST.get('username')
		if len(user)==0:
			result['result'].append('blankUsername')
		query=User.objects.filter(user=user)
		if len(query)==1:
			result['result'].append('userExists')
		
		email=request.POST.get('email')
		query=User.objects.filter(email=email)
		if len(query)==1 and 'userExists' not in result['result']:
			result['result'].append('userExists')
		if len(email)==0:
			result['result'].append('blankEmail')
		elif not validEmail(email):
			result['result'].append('invalidEmail')
		password=request.POST.get('password')
		if len(password)<6:
			result['result'].append('passwordTooShort')
		if len(result['result'])==0:
			salt = uuid.uuid4().hex
			hashedPassword = hashlib.sha512(password+salt).hexdigest()
			try:
				query=User.objects.filter(user=user)
				if len(query)==0:
					query=User.objects.filter(email=email)
					if len(query)==0:	
						try:
							User(user=user.lower(),password=hashedPassword,email=email.lower(),salt=salt).save()
							result['result']='OK'
						except:
							traceback.print_exc()
							result['result']='exception'
					elif len(query)==1:
						result['result'].append('userExists')
					else:
						result['result'].append('somethingWentHorriblyWrongCheckingEmail'	)
						
				elif len(query)==1 and 'userExists' not in result['result']:
					result['result'].append('userExists')
				else:
					result['result'].append('somethingWentHorriblyWrongChecking')
			except:
				traceback.print_exc()
				result['result']='failedChecking'
		return HttpResponse(json.dumps(result))
				
def validEmail(email):
	try:
		pattern=re.compile(r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}$', re.IGNORECASE)
		if re.match(pattern, email) is not None:
			print re.match('^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}$', email)
			return True
		else:
			return False
	except:
		return False
def addAssignment(request):
	c=RequestContext(request)
	sessionId=request.COOKIES.get('sessionId')
	assignmentName=request.POST.get('name')
	assignmentSubject=None #Defined below, the user id was needed which is gotten beow
	assignmentPriority=None #Defined below, the user id was needed which is gotten beow
	result={}
	
	if sessionId!=None:
		sessionQuery=Session.objects.filter(sessionId=sessionId)
		subjectId=request.POST.get('subjectId')
		if len(sessionQuery)==1:
			try:
				assignmentPriority=Homework.objects.filter(userId=sessionQuery[0].userId).order_by('priority')[-1]+1
			except:
				assignmentPriority=0
			if subjectId!='None':
				assignmentSubject=Subject.objects.filter(userId=sessionQuery[0].userId,subjectId=subjectId)
				if len(assignmentSubject)==1:
					uid=uuid.uuid4().hex
					while len(Homework.objects.filter(taskId=uid))>0:
						uid=uuid.uuid4().hex
					assignment=Homework.objects.create(userId=sessionQuery[0].userId,label=assignmentName, subject=assignmentSubject[0], priority=assignmentPriority,taskId=uid)
					assignment.save()
					result['result']='OK'
					result['assignmentName']=assignment.label
					result['assignmentSubject']=assignment.subject.name
					result['assignmentId']=assignment.taskId
				else:
					print assignmentSubject
					print sessionId
					print request.POST.get('subjectId')
					result['result']="somethingWentHorriblyWrong"	
			else:
				result['result']='noSubject'
		else:
			print 'sessionFailed'
			result['result']="somethingWentHorriblyWrong"
	else:
		result['result']="noUserLoggedIn"
	return HttpResponse(json.dumps(result))
def removeAssignment(request):
	c=RequestContext(request)
	taskId=request.POST.get('taskId')
	assignment=Homework.objects.filter(taskId=taskId)
	result={}
	if len(assignment)==1:
		assignment[0].delete()
		result['result']='OK'
	else:
		print 'FAILED'
		print len(assignment)
		print taskId
		result['result']="somethingWentHorriblyWrong"
	return HttpResponse(json.dumps(result))
def addSubject(request):
	c=RequestContext(request)
	subjectName=request.POST.get('subjectName')
	sessionId=request.COOKIES.get('sessionId')
	uid=uuid.uuid4().hex
	result={}
	while len(Subject.objects.filter(subjectId=uid))>0:
		uid=uuid.uuid4().hex	
	if sessionId!=None and len(subjectName)>0:
		sessionQuery=Session.objects.filter(sessionId=sessionId)
		if len(sessionQuery)==1:
			Subject.objects.create(userId=sessionQuery[0].userId, name=subjectName, subjectId=uid).save()
			result['result']='OK'
			result['subjectId']=uid
		else:
			result['result']="somethingWentHorriblyWrong"
	else:
		result['result']="noUserLoggedIn"
	return HttpResponse(json.dumps(result))
def sortTasks(request):
	c=RequestContext(request)
	taskIds=request.POST.getlist('taskIds[]')
	print taskIds
	sessionId=request.COOKIES.get('sessionId')
	result={}
	if sessionId!=None and len(taskIds)>0:
		sessionQuery=Session.objects.filter(sessionId=sessionId)
		if len(sessionQuery)==1:
			assignments=Homework.objects.filter(userId=sessionQuery[0].userId)
			# assignmentIds=[item.taskId for item in assignemnts]
			# sortedAssignments=zip(taskIds,assignmentIds)
			# print sortedAssignments
			print [item.label for item in list(assignments)]
			for item in assignments:
				for task in taskIds:
					if task==item.taskId:
						item.priority=taskIds.index(item.taskId)
						item.save()
						print item.label
						print item.priority
						print list(assignments).index(item)
		return HttpResponse('None');
		