from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from multiprocessing.pool import ThreadPool
from Diaries import models
from boto.s3.key import Key
from django.views.decorators.csrf import csrf_exempt
from StringIO import StringIO
from datetime import datetime
from django.db.models import Q #to allow complex lookups in models
from Diaries.models import User, Achievements, Likes, Comments, Tags
from . import utils
import logging
import PySQLPool
import threading
import time
import tempfile
import json
import string
import random
import requests        
import boto
import os
import urllib2
import urllib

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

@csrf_exempt
def registerUser(request):
    RESULT = 0
    if request.method == "POST":
        NAME= request.POST.get('username')
        EMAIL = request.POST.get('email')
        PASSWORD = request.POST.get('password')
        ACTIVATION_CODE = utils.randomInviteId()
        alreadyExisting = User.objects.filter(Q(User_Name=NAME) | Q(User_Email=EMAIL))
        if len(alreadyExisting)!=0:
        	return HttpResponse(json.dumps({"register":"false","message":"Username/Email already existing"}), content_type="application/json")
    	else:
    		CURRENT_DATE = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    		newUser = User(User_Name=NAME, User_Email = EMAIL, User_Password = PASSWORD, User_Profile_Picture = '', User_About = 'A short description about me', User_Activation_Code = ACTIVATION_CODE, User_Is_Activated = 'False', User_Talent_Score = 0, User_Created_At = CURRENT_DATE, User_Last_Login = CURRENT_DATE, User_Last_Logout = CURRENT_DATE)
    		newUser.save()
    		# SMTP Auth not supported by server
    		# Will run when you deploy on Amazon
    		# utils.sendActivationEmail(EMAIL,ACTIVATION_CODE)
    		return HttpResponse(json.dumps({"register":"True","message":"Successfully Registered"}), content_type="application/json")

def activateUser(request):
	if request.method == "GET":
		EMAIL = request.GET.get('email')
        ACTIVATION_CODE = request.GET.get('act')
        update = User.objects.filter(User_Email=EMAIL, User_Activation_Code = ACTIVATION_CODE).update(User_Is_Activated='True')
        print update
        if update!=0:
	        return HttpResponse(json.dumps({"registerActivation":"True","message":"Successfully User Activated"}), content_type="application/json")
    	else:
	    	return HttpResponse(json.dumps({"registerActivation":"False","message":"User Activation Failed"}), content_type="application/json")
	return HttpResponse(json.dumps({"registerActivation":"False","message":"User Activation Failed"}), content_type="application/json")

@csrf_exempt
def loginUser(request):
	if request.method == "POST":
		EMAIL = request.POST.get('email')
        PASSWORD = request.POST.get('password')
        validCredentials = User.objects.filter(User_Email=EMAIL,User_Password=PASSWORD)
        if len(validCredentials)==1:
	        return HttpResponse(json.dumps({"login":"True","message":"Authentic User Credentials"}), content_type="application/json")
    	else:
	    	return HttpResponse(json.dumps({"login":"False","message":"Incorrect Username/password"}), content_type="application/json")
	return HttpResponse(json.dumps({"login":"False","message":"Incorrect Username/password"}), content_type="application/json")    

@csrf_exempt
def addNewAchievement(request):
    if request.method == "POST":
        TITLE = request.POST.get('ach_title')
        DESCRIPTION = request.POST.get('ach_desc')
        DATE = request.POST.get('ach_date')
        LOCATION = request.POST.get('ach_location')
        CURRENT_DATE = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        newAchievement = Achievements(User_ID=3,Achievement_Title=TITLE, Achievement_Description=DESCRIPTION, Achievement_Date=DATE, Achievement_Location=LOCATION, Achievement_Attachments='', Achievement_Timestamp=CURRENT_DATE)
        newAchievement.save()
        return HttpResponse(json.dumps({"achievements":"True","message":"Successfully Added"}), content_type="application/json")
    return HttpResponse(json.dumps({"achievements":"False","message":"Sorry! Your achievement could not be added"}), content_type="application/json")

@csrf_exempt
def likeAchievement(request):
    if request.method == "POST":
        USER = request.POST.get('user_id')
        ACHIEVEMENT = request.POST.get('achievement_id')
        CURRENT_DATE = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        newLike = Likes(User_ID=USER, Achievement_ID=ACHIEVEMENT, Like_Timestamp=CURRENT_DATE)
        newLike.save()
        return HttpResponse(json.dumps({"like":"True","message":""}), content_type="application/json")
    return HttpResponse(json.dumps({"like":"False","message":"Some error occured. Please try again later."}), content_type="application/json")

@csrf_exempt
def commentAchievement(request):
    if request.method == "POST":
        USER = request.POST.get('user_id')
        ACHIEVEMENT = request.POST.get('achievement_id')
        COMMENT = request.POST.get('comment')
        CURRENT_DATE = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        newComment = Comments(User_ID=USER, Achievement_ID=ACHIEVEMENT,Comment=COMMENT, Comment_Timestamp=CURRENT_DATE)
        newComment.save()
        return HttpResponse(json.dumps({"like":"True","message":""}), content_type="application/json")
    return HttpResponse(json.dumps({"like":"False","message":"Some error occured. Please try again later."}), content_type="application/json")

@csrf_exempt
def tagAchievement(request):
    if request.method == "POST":
        USER = request.POST.get('user_id')
        ACHIEVEMENT = request.POST.get('achievement_id')
        TAG = request.POST.get('tag')
        TAG = TAG.split(' ')
        for x in TAG:
            CURRENT_DATE = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            newTag = Tags(User_ID=USER, Achievement_ID=ACHIEVEMENT,Tag=x, Tag_Timestamp=CURRENT_DATE)
            newTag.save()
        tags = list(Tags.objects.filter(Achievement_ID = ACHIEVEMENT).order_by('Tag_Timestamp').values())
        return HttpResponse(json.dumps({"like":"True","message":tags},default=date_handler), content_type="application/json")
    return HttpResponse(json.dumps({"like":"False","message":"Some error occured. Please try again later."}), content_type="application/json")

@csrf_exempt
def fetchAllComments(request):
    if request.method=="POST":
        ACHIEVEMENT = request.POST.get('achievement_id')
        comments = list(Comments.objects.filter(Achievement_ID = ACHIEVEMENT).order_by('Comment_Timestamp').values())
        print comments
        return HttpResponse(json.dumps(comments,default=date_handler), content_type="application/json")
    return HttpResponse(json.dumps({"comment":"False","message":"Some error occured. Please try again later."},default=date_handler), content_type="application/json")

@csrf_exempt
def viewFeed(request):
    achievements = list(Achievements.objects.all().order_by('Achievement_Timestamp').values())
    print achievements
    return HttpResponse(json.dumps(achievements,default=date_handler), content_type="application/json")    