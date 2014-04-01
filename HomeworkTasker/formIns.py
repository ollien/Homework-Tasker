from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
import json
#this is needed for hashes and salts :D
import hashlib
import uuid

import re

#Here we're just gonna import the models as needed, rather than a messy * import
from models import User
from models import Session

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
		persist=True
		result=userHandling.login(user,password,persist) #Change this from false
		response=HttpResponse(json.dumps(result['result']))
		if (result['result']=='OK'):
			exp=None
			if persist:
				exp=datetime.date.today()+datetime.timedelta(14,0)
			print exp
			response.set_cookie('sessionId',result['sessionId'],path='/',expires=exp)
		return response
# def sessionLogin(request):
#     c=RequestContext(request)
#     try:
# 	    query=Session.objects.filter(sessionId=reqeust.POST.get('sessionId'))
# 	    if len(query)==1:
# 		    #Redirect
# 		    print 'redirecting'
# 		elif len(query)==0:
# 			#Do Nothing
# 			print 'nothing'
# 		elif len(query)>2:
# 			#Horribly wrong
# 			print 'something wnet horribly wrong'
		
        
def registerForm(request):
	c=RequestContext(request)
	result={}
	if request.method=='POST':
		user=request.POST.get('username')
		if len(user)==0:
			result['result']='blankUsername'
		email=request.POST.get('email')
		if len(email)==0:
			result['result']='blankEmail'
		elif not validEmail(email):
			result['result']='invalidEmail'
		password=request.POST.get('password')
		if len(password)<6:
			result['result']='passwordTooShort'
		if result=={}:
			salt = uuid.uuid4().hex
			hashedPassword = hashlib.sha512(password+salt).hexdigest()
			try:
				query=User.objects.filter(user=user)
				if len(query)==0:
					query=User.objects.filter(email=email)
					if len(query)==0:	
						try:
							User(user=user,password=hashedPassword,email=email,salt=salt).save()
							result['result']='OK'
						except:
							traceback.print_exc()
							result['result']='exception'
					elif len(query)==1:
						result['result']='userExists'
					else:
						result['result']='somethingWentHorriblyWrongCheckingEmail'	
						
				elif len(query)==1:
					result['result']='userExists'
				else:
					result['result']='somethingWentHorriblyWrongChecking'
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
