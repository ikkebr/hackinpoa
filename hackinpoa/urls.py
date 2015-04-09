from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static
import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'hackinpoa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('base.urls')),
    url(r'^login', 'django.contrib.auth.views.login',
        {'template_name': 'base/login.html'}, name="login"),
    url(r'^logout', 'django.contrib.auth.views.logout_then_login',
        name="logout"),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.STATIC_URL)
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)))
