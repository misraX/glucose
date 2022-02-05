from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.level.api.filters import UserGlucoseLeveFilterSet
from apps.level.api.serializers import UserGlucoseLevelSerializer
from apps.level.models import UserGlucoseLevel


class LevelModelViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = UserGlucoseLevel.objects.all()
    serializer_class = UserGlucoseLevelSerializer
    filterset_class = UserGlucoseLeveFilterSet
    ordering_fields = '__all__'
