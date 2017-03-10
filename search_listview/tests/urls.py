from django.conf.urls import url

from .views import ListDevicePaginate, ListDeviceSearchablePaginate,\
    ListDeviceReverseRelation, ListDeviceReverseRelationProvider, StandardList

urlpatterns = [
    url(r'^devices$', ListDevicePaginate.as_view(), name='list_device'),
    url(r'^devices/search$', ListDeviceSearchablePaginate.as_view(), name='list_device_searchable'),
    url(r'^provider$', ListDeviceReverseRelationProvider.as_view(), name='list_provider'),
    url(r'^brand$', ListDeviceReverseRelation.as_view(), name='list_brand'),
    url(r'^$', StandardList.as_view(), name='standard_list')
]