from django.contrib import admin

from .models import Provider, Brand, ModelDevice, Device

admin.site.register(Provider)
admin.site.register(Brand)
admin.site.register(ModelDevice)
admin.site.register(Device)