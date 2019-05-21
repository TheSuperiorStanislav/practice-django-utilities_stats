from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.validators import validate_norm


class UtilitiesUser(AbstractUser):
    price_help_text = _("Required. Only numbers greater than zero")

    email = models.EmailField(
        _('email address'),
        unique=True,)

    hws_cold_water_norm = models.FloatField(
        _('HWS Cold Water Norm'),
        null=True,
        blank=False,
        help_text=price_help_text,
        validators=[validate_norm],
    )
    cold_water_norm = models.FloatField(
        _('Cold Water Norm'),
        null=True,
        blank=False,
        help_text=price_help_text,
        validators=[validate_norm],
    )
    sewage_norm = models.FloatField(
        _('Sewage Norm'),
        null=True,
        blank=False,
        help_text=price_help_text,
        validators=[validate_norm],
    )
    electricity_norm = models.FloatField(
        _('Electricity Norm'),
        null=True,
        blank=False,
        help_text=price_help_text,
        validators=[validate_norm],
    )
