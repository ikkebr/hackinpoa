from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^groups/$', GroupList.as_view(), name='groups'),
	url(r'^group/create/$', GroupCreate.as_view(), name="group_create"),
	url(r'^group/(?P<pk>\d+)/detail/$', GroupDetail.as_view(), name="group_all"),
]