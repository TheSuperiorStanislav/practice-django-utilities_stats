import datetime

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import UtilitiesForm
from .models import Utilities


class CreateUtilitiesView(LoginRequiredMixin, CreateView):
    form_class = UtilitiesForm
    success_url = reverse_lazy('utilities:list')
    template_name = 'utilities_create.html'

    def form_valid(self, form):
        owner = self.request.user
        form.instance.owner = owner
        form.instance.date_last_edit = datetime.datetime.now()

        underpayment = form.instance.underpayment
        amount_to_pay = form.instance.amount_to_pay
        payments_last_mouth = form.instance.payments_last_mouth

        form.instance.to_pay = amount_to_pay - (
            payments_last_mouth - underpayment)
        return super(CreateUtilitiesView, self).form_valid(form)


class DetailUtilitiesView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Utilities
    template_name = 'utilities_detail.html'
    context_object_name = 'utilities'

    def test_func(self):
        return self.get_object().owner == self.request.user


class ListUtilitiesView(LoginRequiredMixin, ListView):
    model = Utilities
    template_name = 'utilities_list.html'
    context_object_name = 'utilities_list'

    def get_queryset(self):
        return Utilities.objects.filter(
            owner=self.request.user
        ).order_by(
            '-date'
        )


class EditUtilitiesView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Utilities
    form_class = UtilitiesForm
    success_url = reverse_lazy('utilities:list')
    template_name = 'utilities_edit.html'

    def form_valid(self, form):
        form.instance.date_last_edit = datetime.datetime.now()

        underpayment = form.instance.underpayment
        amount_to_pay = form.instance.amount_to_pay
        payments_last_mouth = form.instance.payments_last_mouth

        form.instance.to_pay = amount_to_pay - (
            payments_last_mouth - underpayment)
        return super(EditUtilitiesView, self).form_valid(form)

    def test_func(self):
        return self.get_object().owner == self.request.user
