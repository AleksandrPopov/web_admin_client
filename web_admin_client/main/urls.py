from django.urls import path
from . import views
from .views import LoginAdmin, logout_admin

urlpatterns = [
    path('', views.index),
    path('login', LoginAdmin.as_view(), name='login'),
    path('logout', logout_admin, name='logout')
]

