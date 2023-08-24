from django.urls import path
from . import views

urlpatterns = [
    path('', views.masters, name='registers'),
]
