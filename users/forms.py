from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UtilitiesUser


class UtilitiesUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UtilitiesUser
        fields = [
            'email',
            'username',
        ]


class UtilitiesUserChangeForm(forms.ModelForm):

    class Meta:
        model = UtilitiesUser
        fields = [
            'first_name',
            'last_name',
            'dark_theme',
            'email',
            'hws_cold_water_norm',
            'cold_water_norm',
            'sewage_norm',
            'electricity_norm',
        ]
