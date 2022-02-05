import django_tables2 as tables

from apps.level.models import UserGlucoseLevel


class UserGlucoseLevelTable(tables.Table):
    """
    User's glucose level table with bootstrap
    """

    class Meta:
        model = UserGlucoseLevel
        template_name = "django_tables2/bootstrap.html"
        fields = [model.name for model in UserGlucoseLevel._meta.get_fields()]
