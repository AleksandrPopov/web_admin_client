from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from address.forms import AddAddressForm
from address.models import Address
from web_admin_client.utils import DataMixin


class AddressView(DataMixin, CreateView):
    form_class = AddAddressForm
    template_name = 'address/address.html'
    context_object_name = 'form'
    success_url = reverse_lazy('address')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Address'
        context['content'] = Address.objects.filter(admins_pk=self.request.user)
        return context


class DeleteAddressView(DeleteView):
    model = Address
    success_url = reverse_lazy('address')


class UpdateAddressView(UpdateView):
    model = Address
    context_object_name = 'form'
    template_name = 'address/address.html'
    fields = ['city', 'street']
    success_url = reverse_lazy('address')
