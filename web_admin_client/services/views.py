from django.shortcuts import render, redirect

from services.forms import AddServicesForm
from services.models import Services
from web_admin_client.menu import menu


def services(request):
    if request.method == 'POST':
        form = AddServicesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('services')
            except:
                form.add_error(None, 'Error')
    else:
        form = AddServicesForm()

    context = {
        'menu': menu,
        'title': 'Services',
        'services': Services.objects.all(),
        'form': form
    }
    return render(request, 'services/services.html', context=context)
