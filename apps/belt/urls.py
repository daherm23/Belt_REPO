from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^travels$', views.index),
	url(r'^travels/destination/(?P<id>\d+)$', views.destination),
	url(r'^travels/add$', views.add_travel),
	url(r'^create$', views.create),
	url(r'^travels/join/(?P<id>\d+)$', views.join) 

  ]