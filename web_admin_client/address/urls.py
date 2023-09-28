from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'', AddressUpdateAPIView)

urlpatterns = [
    # path('', AddressView.as_view(), name='address'),
    # path('/<int:pk>/delete', DeleteAddressView.as_view(), name='address_delete'),
    # path('/<int:pk>/update', AddressUpdateAPIView.as_view(), name='address_update'),
    path('/api/v1/', include(router.urls)),
]