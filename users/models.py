from django.contrib.auth.models import AbstractUser
from django.db import models


class UtilitiesUser(AbstractUser):
    hws_cold_water_norm = models.PositiveIntegerField(null=True, blank=False)
    cold_water_norm = models.PositiveIntegerField(null=True, blank=False)
    sewage_norm = models.PositiveIntegerField(null=True, blank=False)
    electricity_norm = models.PositiveIntegerField(null=True, blank=False)
