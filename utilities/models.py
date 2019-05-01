from django.db import models
from django.db.models import Avg, Max, Min, Sum
from django.utils.translation import gettext_lazy as _
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

from core.validators import validate_price
from users.models import UtilitiesUser


class UtilitiesManager(models.Manager):
    use_for_related_fields = True

    def avg_payments(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Avg('payments_last_mouth'))

    def sum_payments(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Sum('payments_last_mouth'))

    def max_payments(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Max('payments_last_mouth'))

    def min_payments(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Min('payments_last_mouth'))

    def values_payments(self, owner, year):
        return [(query['date'].month, query['payments_last_mouth'])
                for query in
                self.filter(owner=owner, date__year=year).
                values('payments_last_mouth')]

    def avg_hws_cold_water_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Avg('hws_cold_water_consumption'))

    def sum_hws_cold_water_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Sum('hws_cold_water_consumption'))

    def max_hws_cold_water_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Max('hws_cold_water_consumption'))

    def min_hws_cold_water_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Min('hws_cold_water_consumption'))

    def values_hws_cold_water_consumption(self, owner, year):
        return [(query['date'].month, query['hws_cold_water_consumption'])
                for query in
                self.filter(owner=owner, date__year=year).
                values('hws_cold_water_consumption')]

    def avg_cold_water_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Avg('cold_water_consumption'))

    def sum_cold_water_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Sum('cold_water_consumption'))

    def max_cold_water_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Max('cold_water_consumption'))

    def min_cold_water_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Min('cold_water_consumption'))

    def values_cold_water_consumption(self, owner, year):
        return [(query['date'].month, query['cold_water_consumption'])
                for query in
                self.filter(owner=owner, date__year=year).
                values('cold_water_consumption')]

    def avg_sewage_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Avg('sewage_consumption'))

    def sum_sewage_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Sum('sewage_consumption'))

    def max_sewage_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Max('sewage_consumption'))

    def min_sewage_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Min('sewage_consumption'))

    def values_sewage_consumption(self, owner, year):
        return [(query['date'].month, query['sewage_consumption'])
                for query in
                self.filter(owner=owner, date__year=year).
                values('sewage_consumption')]

    def avg_electricity_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Avg('electricity_consumption'))

    def sum_electricity_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Sum('electricity_consumption'))

    def max_electricity_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Max('electricity_consumption'))

    def min_electricity_consumption(self, owner, year):
        return self.filter(owner=owner, date__year=year).aggregate(
            Min('electricity_consumption'))

    def values_electricity_consumption(self, owner, year):
        return [(query['date'].month, query['electricity_consumption'])
                for query in
                self.filter(owner=owner, date__year=year).
                values('date', 'electricity_consumption')]


class Utilities(models.Model):
    price_help_text = "Required. Only numbers greater than zero"

    objects = UtilitiesManager()
    owner = models.ForeignKey(
        UtilitiesUser,
        on_delete=models.CASCADE
    )

    date = models.DateField()
    date_added = models.DateTimeField(
        auto_now_add=True,
        null=False)
    date_last_edit = models.DateTimeField(
        null=False)

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
