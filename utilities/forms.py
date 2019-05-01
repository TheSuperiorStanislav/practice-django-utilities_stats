from django import forms
from django.forms import ModelForm

from .models import Utilities

form_fields = [
    'date',
    'underpayment',
    'amount_to_pay',
    'payments_last_mouth',
    'housing_stock',
    'hws_thermal_energy_cp',
    'hws_cold_water_cp',
    'cold_water_cp',
    'sewage_cp',
    'electricity_cp',
    'special_account_for_overhaul',
    'home_heating',
    'hws_thermal_energy',
    'hws_cold_water',
    'cold_water',
    'sewage',
    'garbage_service',
    'electricity',
    'intercom_maintenance',
    'gate_maintenance',
    'cctv_maintenance',
    'hws_cold_water_consumption',
    'cold_water_consumption',
    'sewage_consumption',
    'electricity_consumption',
]


class DateInput(forms.DateInput):
    input_type = 'date'


class UtilitiesForm(ModelForm):

    class Meta:
        model = Utilities
        fields = form_fields
        widgets = {
            'date': DateInput(),
        }