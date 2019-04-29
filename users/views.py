from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UtilitiesUserCreationForm


class SignUpView(CreateView):
    form_class = UtilitiesUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
