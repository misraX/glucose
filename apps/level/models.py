from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.abstract_models import AbstractBaseModel
from apps.device.models import GlucoseDevice

User = get_user_model()


class UserGlucoseLevel(AbstractBaseModel):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    level = models.IntegerField(_("level"))
    device = models.ForeignKey(GlucoseDevice, verbose_name=_("Device"), on_delete=models.CASCADE)

    class Meta:
        db_table = "user_glucose_level"
        ordering = ['-created']
