from django.shortcuts import render
from web_admin_client.menu import menu



def schedules(request):
    context = {
        'menu': menu,
        'title': 'Schedules'
    }
    return render(request, 'schedules/schedules.html', context=context)
