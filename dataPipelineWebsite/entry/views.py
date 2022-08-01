import csv

from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from dataPipelineWebsite.entry.forms import DataEntryForm
from dataPipelineWebsite.entry.models import Data


class DataEntryFormView(FormView):
    form_class = DataEntryForm
    success_url = reverse_lazy('success')
    template_name = 'form.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'success.html'
