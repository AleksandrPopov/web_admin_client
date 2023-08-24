from django.shortcuts import render
from web_admin_client.menu import menu


def history(request):
    context = {
        'menu': menu,
        'title': 'History'
    }
    return render(request, 'history/history.html', context=context)
