from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from web_admin_client.menu import menu


class AddressDataMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = kwargs
        if self.request.user.is_authenticated:
            context['menu'] = menu
        return context

    def form_valid(self, form):
        form.instance.admins_pk = self.request.user
        return super().form_valid(form)
