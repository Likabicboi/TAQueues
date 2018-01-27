from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^CMSC[0-9]+$', views.submit, name='submit'),
	]