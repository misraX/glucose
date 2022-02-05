import uuid as uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class AbstractBaseModel(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    meta = models.JSONField(_("meta"), null=True, blank=True)

    class Meta:
        abstract = True
