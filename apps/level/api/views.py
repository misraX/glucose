from rest_framework import viewsets

from apps.level.api.serializers import UserGlucoseLevelSerializer
from apps.level.models import UserGlucoseLevel


class LevelModelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = UserGlucoseLevel.objects.all()
    serializer_class = UserGlucoseLevelSerializer
