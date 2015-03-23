from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.utils.functional import curry
from django.views.defaults import *
from Diaries import views

urlpatterns = patterns('',
    url(r'^registerUser/', views.registerUser, name='registerUser'),
    url(r'^activateUser/', views.activateUser, name='activateUser'),
    url(r'^loginUser/', views.loginUser, name='loginUser'),
    url(r'^viewFeed/', views.viewFeed, name='viewFeed'),
	url(r'^addNewAchievement/', views.addNewAchievement, name='addNewAchievement'),
	url(r'^likeAchievement/', views.likeAchievement, name='likeAchievement'),
	url(r'^commentAchievement/', views.commentAchievement, name='commentAchievement'),
	url(r'^tagAchievement/', views.tagAchievement, name='tagAchievement'),
	url(r'^fetchComments/', views.fetchAllComments, name='fetchAllComments')
)
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handler500 = views.handler500
# handler404 = views.handler404
# https://scontent-a.xx.fbcdn.net/hphotos-xpa1/t31.0-8/10872898_10154932564135324_1070067102469879988_o.jpg