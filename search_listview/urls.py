from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from django.shortcuts import redirect

admin.autodiscover()

urlpatterns = [
    url(r'^$', lambda request : redirect("standard_list")),
    url(r'^list/', include('search_listview.tests.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

# debug toolbar for dev
if settings.DEBUG and 'debug_toolbar'in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
