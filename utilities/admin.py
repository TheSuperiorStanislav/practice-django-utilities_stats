from django.contrib import admin

from .forms import UtilitiesForm
from .models import Utilities


class UtilitiesAdmin(admin.ModelAdmin):
    add_form = UtilitiesForm
    form = UtilitiesForm
    model = Utilities
    list_display = ['date', ]


admin.site.register(Utilities, UtilitiesAdmin)
