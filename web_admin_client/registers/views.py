from django.shortcuts import render
from django.views.generic import CreateView

from web_admin_client.menu import menu
from web_admin_client.utils import DataMixin


class RegistersView(DataMixin, CreateView):
    # form_class = AddAddressForm
    template_name = 'registers/registers.html'
    # context_object_name = 'form'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
