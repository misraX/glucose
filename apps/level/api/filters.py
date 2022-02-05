from django_filters import FilterSet, filters

from apps.level.models import UserGlucoseLevel


class UserGlucoseLeveFilterSet(FilterSet):
    """
    Filter for user's glucose level mode
    """
    start = filters.DateFilter(lookup_expr="gte", field_name="device_timestamp", label="start")
    stop = filters.DateFilter(lookup_expr="lte", field_name="device_timestamp", label="stop")

    class Meta:
        model = UserGlucoseLevel
        fields = [
            "user",
            "start",
            "stop",
        ]
