from django.db import models
from django.db.models import Avg, Max, Min, Sum
from django.utils.translation import gettext_lazy as _
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

from core.validators import validate_price
from users.models import UtilitiesUser


class UtilitiesManager(models.Manager):
    use_for_related_fields = True

    def get_by_owner_year(self, owner, year):
        return self.filter(owner=owner, date__year=year).order_by('date')

    def avg_field(self, owner, year, field):
        return round(self.get_by_owner_year(owner, year).aggregate(
            Avg(field))['%s__avg' % field], 3)

    def sum_field(self, owner, year, field):
        return self.get_by_owner_year(owner, year).aggregate(
            Sum(field))['%s__sum' % field]

    def max_field(self, owner, year, field):
        return self.get_by_owner_year(owner, year).aggregate(
            Max(field))['%s__max' % field]

    def min_field(self, owner, year, field):
        return self.get_by_owner_year(owner, year).aggregate(
            Min(field))['%s__min' % field]

    def values_field(self, owner, year, field):
        return [(query['date'].month, round(query[field], 3))
                for query in self.get_by_owner_year(owner, year)
                .values('date', field)]


class Utilities(models.Model):
    price_help_text = _("Required. Only numbers greater than zero")

    objects = UtilitiesManager()
    owner = models.ForeignKey(
        UtilitiesUser,
        on_delete=models.CASCADE
    )

    date = models.DateField(
        _('Date'),
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        null=False)
    date_last_edit = models.DateTimeField(
        auto_now=True
        )

    underpayment = models.FloatField(
        _('Underpayment'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    amount_to_pay = models.FloatField(
        _('Amount to pay'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    payments_last_mouth = models.FloatField(
        _('Payments last mouth'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    to_pay = models.FloatField(
        _('To pay'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    housing_stock = models.FloatField(
        _('Housing Stock'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    hws_thermal_energy_cp = models.FloatField(
        _('HWS: Thermal energy CP'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    hws_cold_water_cp = models.FloatField(
        _('HWS: Cold Water CP'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    cold_water_cp = models.FloatField(
        _('Cold Water CP'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    sewage_cp = models.FloatField(
        _('Sewage CP'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    electricity_cp = models.FloatField(
        _('Electricity CP'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    special_account_for_overhaul = models.FloatField(
        _('Special account for overhaul'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    home_heating = models.FloatField(
        _('Home Heating'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    hws_thermal_energy = models.FloatField(
        _('HWS: Thermal Energy'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    hws_cold_water = models.FloatField(
        _('HWS: Cold Water'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    cold_water = models.FloatField(
        _('Cold Water'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    sewage = models.FloatField(
        _('Sewage'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    garbage_service = models.FloatField(
        _('Garbage service'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    electricity = models.FloatField(
        _('Electricity'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    intercom_maintenance = models.FloatField(
        _('Intercom Maintenance'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    gate_maintenance = models.FloatField(
        _('Gate Maintenance'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    cctv_maintenance = models.FloatField(
        _('CCTV Maintenance'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )

    hws_cold_water_consumption = models.FloatField(
        _('HWS: Cold Water Consumption'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    cold_water_consumption = models.FloatField(
        _('Cold Water Consumption'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    sewage_consumption = models.FloatField(
        _('Sewage Consumption'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )
    electricity_consumption = models.FloatField(
        _('Electricity Consumption'),
        null=False,
        blank=False,
        help_text=price_help_text,
        validators=[validate_price],
    )

    def __str__(self):
        df = DateFormat(self.date)
        return df.format(get_format('DATE_FORMAT'))
