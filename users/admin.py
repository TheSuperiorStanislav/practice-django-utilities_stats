from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UtilitiesUserCreationForm, UtilitiesUserChangeForm
from .models import UtilitiesUser


class UtilitiesUserAdmin(UserAdmin):
    add_form = UtilitiesUserCreationForm
    form = UtilitiesUserChangeForm
    model = UtilitiesUser
    list_display = ['username', 'is_staff', 'electricity_norm', ]


admin.site.register(UtilitiesUser, UtilitiesUserAdmin)
