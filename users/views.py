from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import UtilitiesUserCreationForm
from .models import UtilitiesUser


class SignUpView(CreateView):
    form_class = UtilitiesUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class EditProfileView(UpdateView):
    model = UtilitiesUser
    fields = [
        'first_name',
        'last_name',
        'hws_cold_water_norm',
        'cold_water_norm',
        'sewage_norm',
        'electricity_norm'
        ]
    success_url = reverse_lazy('home')
    template_name = 'edit_profile.html'
