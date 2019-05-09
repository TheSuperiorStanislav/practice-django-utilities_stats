from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import UtilitiesUserCreationForm
from .models import UtilitiesUser


class SignUpView(CreateView):
    form_class = UtilitiesUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class DetailUserView(LoginRequiredMixin, DetailView):
    model = UtilitiesUser
    template_name = 'user_detail.html'
    context_object_name = 'utilities_user'

    def get_context_data(self, **kwargs):
        ctx = super(DetailUserView, self).get_context_data(**kwargs)
        ctx['can_edit'] = self.get_object() == self.request.user
        return ctx

    def get_object(self):
        return UtilitiesUser.objects.get(username=self.kwargs.get("username"))


class EditUserView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UtilitiesUser
    fields = [
        'first_name',
        'last_name',
        'email',
        'hws_cold_water_norm',
        'cold_water_norm',
        'sewage_norm',
        'electricity_norm'
        ]
    template_name = 'user_edit.html'
    context_object_name = 'utilities_user'

    def get_success_url(self):
        return reverse("users:detail", kwargs={
            "username": self.kwargs.get("username")})

    def get_object(self):
        return UtilitiesUser.objects.get(username=self.kwargs.get("username"))

    def test_func(self):
        return self.get_object() == self.request.user
