from django_tables2 import SingleTableView
from django_filters.views import FilterView

# Create your views here.
from apps.level.api.filters import UserGlucoseLeveFilterSet
from apps.level.models import UserGlucoseLevel
from apps.level.tables import UserGlucoseLevelTable


class UserGlucoseLevelListView(SingleTableView, FilterView):
    model = UserGlucoseLevel
    table_class = UserGlucoseLevelTable
    template_name = 'levels.html'
    filterset_class = UserGlucoseLeveFilterSet
