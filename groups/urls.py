from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^$', GroupList.as_view(), name='groups'),
	url(r'^create/$', GroupCreate.as_view(), name="group_create"),
	url(r'^(?P<pk>\d+)/detail/$', GroupDetail.as_view(), name="group_details"),
	url(r'^(?P<pk>\d+)/members/add$', 'groups.views.add_group_members', name="group_add_members"),
	url(r'^(?P<pk>\d+)/join$', 'groups.views.join_group', name="join_group"),
	url(r'^(?P<pk>\d+)/leave$', 'groups.views.leave_group', name="leave_group"),
]