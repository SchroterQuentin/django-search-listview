from search_listview.list import SearchableListView
from .models import Device, Provider, Brand

class ListDevicePaginate(SearchableListView):
    model = Device
    queryset = Device.objects.select_related("model_device", "model_device__brand", "model_device__brand").prefetch_related("model_device__brand__provider")
    template_name = "tests/list.html"
    paginate_by = 10
    

class ListDeviceSearchablePaginate(SearchableListView):
    model = Device
    queryset = Device.objects.select_related("model_device", "model_device__brand", "model_device__brand").prefetch_related("model_device__brand__provider")
    template_name = "tests/list.html"
    paginate_by = 10
    specifications = {
        "model_device__brand__name": "__icontains"
    }
    searchable_fields = ["inventory_number", "model_device", "model_device__brand__provider",
    "model_device__brand__name"]

class ListDeviceReverseRelationProvider(SearchableListView):
    model = Provider
    template_name = "tests/list_reverse.html"
    paginate_by = 2
    searchable_fields = ["brand", "brand__modeldevice__device"]

class ListDeviceReverseRelation(SearchableListView):
    model = Brand
    template_name = "tests/list_reverse_brand.html"
    paginate_by = 2
    searchable_fields = ["modeldevice", "modeldevice__device__inventory_number", "provider"]

class StandardList(SearchableListView):
    model = Device
    queryset = Device.objects.select_related("model_device", "model_device__brand", "model_device__brand").prefetch_related("model_device__brand__provider")
    template_name = "tests/list.html"
    searchable_fields = ["inventory_number", "model_device", "model_device__brand__provider",
    "model_device__brand__name"]