from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import UtilitiesUserCreationForm, UtilitiesUserChangeForm
from .models import UtilitiesUser


class SignUpView(UserPassesTestMixin, CreateView):
    form_class = UtilitiesUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def test_func(self):
        return not self.request.user.is_authenticated


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
    form_class = UtilitiesUserChangeForm
    template_name = 'user_edit.html'
    context_object_name = 'utilities_user'

    def get_success_url(self):
        return reverse("users:detail", kwargs={
            "username": self.kwargs.get("username")})

    def get_object(self):
        return UtilitiesUser.objects.get(username=self.kwargs.get("username"))

    def test_func(self):
        return self.get_object() == self.request.user
