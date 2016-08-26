from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from .views import home

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    # url(r'^app/', include('apps.app.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

# debug toolbar for dev
if settings.DEBUG and 'debug_toolbar'in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
