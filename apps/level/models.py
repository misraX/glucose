from django.contrib.auth import get_user_model
from django.db import models

from apps.core.abstract_models import AbstractBaseModel

User = get_user_model()


class GlucoseLevel(AbstractBaseModel):
    user = models.ForeignKey(_("User"), User, on_delete=models.CASCADE)
    level = models.In
