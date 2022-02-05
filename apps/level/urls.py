from rest_framework.routers import DefaultRouter

from apps.level.api.views import LevelModelViewSet

router = DefaultRouter()
router.register(r'levels', LevelModelViewSet, basename='level')
urlpatterns = router.urls
