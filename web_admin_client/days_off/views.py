from django.shortcuts import render
from web_admin_client.menu import menu


def days_off(request):
    context = {
        'menu': menu,
        'title': 'Days off'
    }
    return render(request, 'days_off/days_off.html', context=context)
