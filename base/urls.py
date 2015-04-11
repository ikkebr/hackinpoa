from django.conf.urls import include, url

urlpatterns = [
    url('^$', 'base.views.index', name='index'),
    url('^signup', 'base.views.signup', name='signup'),
    url('^profile$', 'base.views.profile', name='profile'),
    url('^profile/edit$', 'users.views.edit_profile', name='edit_profile'),
]
