from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^CMSC(?P<oid>[0-9]+)$', views.submit, name='submit'),
	url(r'dash/(?P<tid>.+)$', views.tadash, name='tadash'),
	url(r'queue/(?P<id>\w+)$', views.queue, name='queue'),
	url(r'login$', views.talogin, name='talogin'),
	]