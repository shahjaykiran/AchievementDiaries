from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Achievement.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^Diaries/', include('Diaries.urls', namespace="Diaries")),
    url(r'^admin/', include(admin.site.urls)),
)
