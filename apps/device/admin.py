from django.contrib import admin

# Register your models here.
from apps.device.models import GlucoseDevice


@admin.register(GlucoseDevice)
class GlucoseDeviceModelAdmin(admin.ModelAdmin):
    pass
