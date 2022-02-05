from django.urls import path

from apps.level.views import UserGlucoseLevelListView

urlpatterns = [
    path('levels/', UserGlucoseLevelListView.as_view(), )
]
