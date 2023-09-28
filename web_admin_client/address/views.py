from address.models import Address
from address.serializers import AddressSerializer
from rest_framework import viewsets


class AddressUpdateAPIView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(admins_pk=self.request.user)
