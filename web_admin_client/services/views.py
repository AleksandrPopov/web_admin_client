from services.models import Services
from services.serializers import ServicesSerializer
from rest_framework import viewsets


class ServicesAPIView(viewsets.ModelViewSet):
    serializer_class = ServicesSerializer

    def get_queryset(self):
        return Services.objects.filter(categories_pk__admins_pk=self.request.user.pk)
