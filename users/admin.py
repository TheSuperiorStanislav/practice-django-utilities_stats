from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UtilitiesUserCreationForm, UtilitiesUserChangeForm
from .models import UtilitiesUser


class UtilitiesUserAdmin(UserAdmin):
    add_form = UtilitiesUserCreationForm
    form_class = UtilitiesUserChangeForm
    model = UtilitiesUser
    list_display = ['username', 'is_staff', ]


admin.site.register(UtilitiesUser, UtilitiesUserAdmin)
