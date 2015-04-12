from django.conf.urls import include, url
from .views import *

urlpatterns = [
    # url(r'^$', GroupList.as_view(), name='groups'),
    url(r'^create/$', CreateTrip.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/route$', CreateRoute.as_view(), name="create-route")
]