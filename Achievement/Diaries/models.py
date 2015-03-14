import datetime
from django.db import models
from django.utils import timezone

class User(models.Model):
	User_ID = models.AutoField(primary_key=True)
	User_Name = models.CharField(max_length=20)
	User_Email = models.CharField(max_length=150)
	User_Password = models.CharField(max_length=50)
	User_Profile_Picture = models.CharField(max_length=50)
	User_About = models.CharField(max_length=500)
	User_Activation_Code = models.CharField(max_length=16)
	User_Is_Activated = models.CharField(max_length=6)
	User_Talent_Score = models.IntegerField(default=0)
	User_Created_At = models.DateTimeField('date created')
	User_Last_Login = models.DateTimeField('date last login')
	User_Last_Logout = models.DateTimeField('date last logout')

class Achievements(models.Model):
	Achievement_ID = models.AutoField(primary_key=True)
	User_ID = models.IntegerField(default=0)
	Achievement_Title = models.CharField(max_length=200)
	Achievement_Description = models.TextField()
	Achievement_Date = models.DateTimeField('Achievement Accomplished')
	Achievement_Location = models.CharField(max_length=150)
	Achievement_Attachments = models.TextField() 
	Achievement_Timestamp = models.DateTimeField('date created')

class Attachments(models.Model):
	Attachment_ID = models.AutoField(primary_key=True)
	Achievement_ID = models.IntegerField(default=0)
	Attachment_URL = models.CharField(max_length=200)
	Attachment_Type = models.CharField(max_length=20)

class Likes(models.Model):
	Like_ID = models.AutoField(primary_key=True)
	User_ID = models.IntegerField(default=0)
	Achievement_ID = models.IntegerField(default=0) 
	Like_Timestamp = models.DateTimeField('date created')

class Comments(models.Model):
	Comment_ID = models.AutoField(primary_key=True)
	User_ID = models.IntegerField(default=0)
	Achievement_ID = models.IntegerField(default=0)
	Comment = models.TextField()
	Comment_Timestamp = models.DateTimeField('date created')

class Tags(models.Model):
	Tag_ID = models.AutoField(primary_key=True)
	User_ID = models.IntegerField(default=0)
	Achievement_ID = models.IntegerField(default=0)
	Tag = models.CharField(max_length=50)
	Tag_Timestamp = models.DateTimeField('date created')

