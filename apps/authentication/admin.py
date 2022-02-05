from django.contrib import admin

from apps.authentication.models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    pass
