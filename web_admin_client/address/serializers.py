from rest_framework import serializers

from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    admins_pk = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Address
        fields = ('id', 'city', 'street', 'house', 'admins_pk')
