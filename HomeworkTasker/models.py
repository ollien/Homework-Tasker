from django.db import models

class User(models.Model):
	user=models.TextField()
	password=models.TextField()
	email=models.TextField()
	salt=models.TextField()
class Session(models.Model):
	sessionId=models.TextField()
	userId=models.ForeignKey(User)
	persist=models.BooleanField()
	accessed=models.DateField()
	