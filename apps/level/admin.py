from django.contrib import admin

# Register your models here.
from apps.level.models import UserGlucoseLevel


@admin.register(UserGlucoseLevel)
class UserGlucoseLevelModelAdmin(admin.ModelAdmin):
    pass
