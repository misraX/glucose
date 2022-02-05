from rest_framework.routers import DefaultRouter

from apps.level.api.views import UserGlucoseLevelModelViewSet

router = DefaultRouter()
router.register(r'levels', UserGlucoseLevelModelViewSet, basename='level')
urlpatterns = router.urls
