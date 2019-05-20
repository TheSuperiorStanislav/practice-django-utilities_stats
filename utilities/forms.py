from django import forms
from django.forms import ModelForm

from .models import Utilities
from .utils import is_data_validation_error, is_date_validation_error

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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.pk = kwargs.pop('pk', None)
        super(UtilitiesForm, self).__init__(*args, **kwargs)

    def clean_date(self):
        date = self.cleaned_data['date']
        if self.pk:
            edit_utilities = Utilities.objects.get(pk=self.pk)
            if date.month == edit_utilities.date.month:
                return date
        error = is_date_validation_error(self.user, date)
        if error:
            msg = u'This entry(%s) already exists!' % (error)
            raise forms.ValidationError(msg)

        return date

    def clean(self):
        cleaned_data = super().clean()
        error = is_data_validation_error(cleaned_data)
        if error:
            raise forms.ValidationError(error)
