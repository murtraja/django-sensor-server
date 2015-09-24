from django.conf.urls import patterns, url
from post import views

urlpatterns = patterns('',
    url(r'^$', views.postData, name= 'post'),
    url(r'^monitor/$', views.monitorData, name = 'monitor'),
    url(r'^download/$', views.downloadAPK, name = 'download'))