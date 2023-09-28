from django.urls import reverse_lazy
from django.views.generic import CreateView

from categories.forms import AddCategoriesForm
from categories.models import Categories


class CategoriesView(CreateView):
    form_class = AddCategoriesForm
    template_name = 'categories/categories.html'
    context_object_name = 'form'
    success_url = reverse_lazy('categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Categories'
        context['content'] = Categories.objects.all()
        return context

