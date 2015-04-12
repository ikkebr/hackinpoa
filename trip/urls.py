from django.conf.urls import include, url
from .views import *

urlpatterns = [
    # url(r'^$', GroupList.as_view(), name='groups'),
    url(r'^create/$', CreateTrip.as_view(), name="create"),
    url(r'^create2/$', CreateTrip_.as_view(), name="create"),
    # url(r'^(?P<pk>\d+)/detail/$', GroupDetail.as_view(), name="group_details"),
]