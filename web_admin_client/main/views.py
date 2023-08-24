from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from main.forms import LoginForm


def index(request):
    # context = {
    #     'menu': menu,
    # }
    return render(request, 'main/main.html')


class LoginAdmin(LoginView):
    form_class = LoginForm
    template_name = 'main/login.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def logout_admin(request):
    logout(request)
    return redirect('login')
