from models import User
from models import Session
import uuid
import hashlib
import datetime
def login(user,password,persist):
		query=User.objects.filter(user=user)
		result={}
		if len(query)==0:
			query=User.objects.filter(email=user)
			if len(query)==0:
				result['result']='userDoesNotExist'
		if len(query)==1:
			usersPassword=query[0].password
			usersSalt=query[0].salt
			if (hashlib.sha512(password+usersSalt).hexdigest()==usersPassword):
				result['result']='OK'
				result.update(createSession(query[0],persist))
			else:
				result['result']='invalidCredentials'
		elif len(query)>1:
			result['result']='somethingWentHorriblyWrong'
		return result
def createSession(user,persist):
	sessionId=hashlib.sha512(user.user+(uuid.uuid4().hex)).hexdigest()
	while len(Session.objects.filter(sessionId=sessionId))!=0:
		sessionId=hashlib.sha512(user.user+(uuid.uuid4().hex)).hexdigest()
	Session(userId=user,sessionId=sessionId,persist=persist,accessed=datetime.date.today()).save()
	return {'sessionId':sessionId}