from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

menu = [
    {'title': 'Address', 'url': 'address', 'btn': 'bi bi-geo-alt'},
    {'title': 'Masters', 'url': 'masters', 'btn': 'bi bi-people'},
    {'title': 'Registers', 'url': 'registers', 'btn': 'bi bi-calendar-week'},
    {'title': 'Schedules', 'url': 'schedules', 'btn': 'bi bi-clock'},
    {'title': 'Days Off', 'url': 'days_off', 'btn': 'bi bi-emoji-sunglasses'},
    {'title': 'Categories', 'url': 'categories', 'btn': 'bi bi-emoji-sunglasses'},
    {'title': 'Services', 'url': 'services', 'btn': 'bi bi-book'},
    {'title': 'History', 'url': 'history', 'btn': 'bi bi-clock-history'}
]


class DataMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = kwargs
        if self.request.user.is_authenticated:
            context['menu'] = menu
        return context

    def form_valid(self, form):
        form.instance.admins_pk = self.request.user
        return super().form_valid(form)
