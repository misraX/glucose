from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.abstract_models import AbstractBaseModel


class GlucoseDevice(AbstractBaseModel):
    name = models.CharField(_("Name"), max_length=250)
    serial = models.CharField(_("Serial #"), max_length=64, unique=True)

    class Meta:
        db_table = "glucose_device"
        ordering = ['-created']

    def __str__(self):
        return f"{self.name}"
