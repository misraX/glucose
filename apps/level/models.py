from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.abstract_models import AbstractBaseModel
from apps.device.models import GlucoseDevice

User = get_user_model()


class UserGlucoseLevel(AbstractBaseModel):
    """
    Recorded user's glucose leve per device
    """
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    device = models.ForeignKey(GlucoseDevice, verbose_name=_("Device"), on_delete=models.CASCADE)
    device_timestamp = models.DateTimeField(_("Device Timestamp"), null=True)
    recording_type = models.CharField(_("Recording Type"), default=0)
    level = models.IntegerField(_("Glucose value history mg/dL"))
    scan = models.IntegerField(_("Glucose-Scan mg/dL"), null=True)
    non_numeric_rapid_insulin = models.CharField(_("Non-numeric rapid-acting insulin"), null=True)
    rapid_acting_insulin = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    non_numeric_nutritional_data = models.CharField(_("Non-numeric nutritional data"), null=True)
    carbohydrates = models.DecimalField(_("Carbohydrates"), max_digits=5, decimal_places=2, null=True)
    non_numeric_depot_insulin = models.CharField(_("Non-numeric depot insulin"), null=True)
    depot_insulin = models.DecimalField(_("Depot insulin (units)"), max_digits=5, decimal_places=2, null=True)
    notes_Glucose_test = models.IntegerField(_("Notes Glucose test strips mg/dL"), null=True)
    ketone = models.DecimalField(_("Ketone mmol/L"), max_digits=5, decimal_places=2, null=True)
    meal_insulin = models.DecimalField(_("Meal Insulin (units)"), max_digits=5, decimal_places=2, null=True)
    correction_insulin = models.DecimalField(_("Correction insulin (units)"), max_digits=5, decimal_places=2, null=True)
    insulin_Change = models.DecimalField(_("User Insulin Change (Units)"), max_digits=5, decimal_places=2, null=True)

    class Meta:
        db_table = "user_glucose_level"
        ordering = ['-created']
