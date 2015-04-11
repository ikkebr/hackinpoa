from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^$', GroupList.as_view(), name='groups'),
	url(r'^create/$', GroupCreate.as_view(), name="group_create"),
	url(r'^(?P<pk>\d+)/detail/$', GroupDetail.as_view(), name="group_details"),
]