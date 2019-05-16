import json

from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.template.defaulttags import register
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import UtilitiesForm
from .models import Utilities

from celery import group
from core.tasks import get_field_data

# Custom tag for dict
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# Custom tag to format field
@register.filter
def format_field(field):
    return field.replace('_', ' ').capitalize().replace('Hws', 'HWS')


@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))


def get_stat_data(owner, fields):
    years_query_set = Utilities.objects.filter(owner=owner).distinct(
            'date__year'
            ).values_list(
                'date__year', flat=True)
    years = [year for year in years_query_set][::-1]

    stat_data = {field: {} for field in fields}
    job = group([
        get_field_data.s(owner.pk, field, years)
        for field in fields
    ])
    result = job.apply_async()
    data = result.join()
    for pair in data:
        stat_data[pair[0]] = pair[1]
    return stat_data


def is_stat_data_empty(stat_data):
    return all(value == {} for value in stat_data.values())


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super(TemplateView, self).get_context_data(**kwargs)
        user = self.request.user
        stat_data = get_stat_data(
            user,
            [
                'amount_to_pay',
                'hws_cold_water_consumption',
                'cold_water_consumption',
                'sewage_consumption',
                'electricity_consumption',
            ]
        )
        ctx['stat_data'] = stat_data
        ctx['is_stat_data_empty'] = is_stat_data_empty(stat_data)
        return ctx


class CreateUtilitiesView(LoginRequiredMixin, CreateView):
    form_class = UtilitiesForm
    success_url = reverse_lazy('utilities:list')
    template_name = 'utilities_create.html'

    def get_form_kwargs(self):
        kwargs = super(CreateUtilitiesView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        owner = self.request.user
        form.instance.owner = owner

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
    paginate_by = 6

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

    def get_form_kwargs(self):
        kwargs = super(EditUtilitiesView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        underpayment = form.instance.underpayment
        amount_to_pay = form.instance.amount_to_pay
        payments_last_mouth = form.instance.payments_last_mouth

        form.instance.to_pay = amount_to_pay - (
            payments_last_mouth - underpayment)
        return super(EditUtilitiesView, self).form_valid(form)

    def test_func(self):
        return self.get_object().owner == self.request.user


class DeleteUtilitiesView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Utilities
    success_url = reverse_lazy('utilities:list')

    def test_func(self):
        return self.get_object().owner == self.request.user
