from django.urls import path
from .views import RegistersView

urlpatterns = [
    path('', RegistersView.as_view(), name='registers')
]
