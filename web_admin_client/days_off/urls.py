from django.urls import path
from . import views

urlpatterns = [
    path('', views.days_off, name='days_off'),

]

