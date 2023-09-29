from categories.models import Categories
from categories.serializers import CategoriesSerializer
from rest_framework import viewsets


class CategoriesAPIView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

    def get_queryset(self):
        return Categories.objects.filter(admins_pk=self.request.user)
