from django.shortcuts import render
from web_admin_client.menu import menu


def masters(request):
    context = {
        'menu': menu,
        'title': 'Masters'
    }
    return render(request, 'masters/masters.html', context=context)

