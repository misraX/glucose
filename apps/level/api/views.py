from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.level.api.filters import UserGlucoseLeveFilterSet
from apps.level.api.serializers import UserGlucoseLevelSerializer
from apps.level.models import UserGlucoseLevel


class UserGlucoseLevelModelViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    """
   User's glucose level per device

   You can filter by start and stop

   Order by any field
    """
    queryset = UserGlucoseLevel.objects.all()
    serializer_class = UserGlucoseLevelSerializer
    filterset_class = UserGlucoseLeveFilterSet
    ordering_fields = '__all__'
