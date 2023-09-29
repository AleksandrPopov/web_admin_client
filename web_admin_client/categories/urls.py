from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'', CategoriesAPIView)

urlpatterns = [
    path('/api/v1/', include(router.urls)),
]