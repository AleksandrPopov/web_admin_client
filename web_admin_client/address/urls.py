from django.urls import path
from .views import *


urlpatterns = [
    path('', AddressView.as_view(), name='address'),
    path('/<int:pk>/delete', DeleteAddressView.as_view(), name='address_delete'),
    path('/<int:pk>/update', UpdateAddressView.as_view(), name='address_update')
]