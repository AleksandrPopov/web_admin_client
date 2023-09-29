from rest_framework import serializers

from categories.models import Categories
from services.models import Services


class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = ('id', 'name', 'time', 'cost', 'categories_pk')

    def __init__(self, *args, **kwargs):
        super(ServicesSerializer, self).__init__(*args, **kwargs)
        user_owner = self.context['request'].user.pk
        self.fields['categories_pk'].queryset = Categories.objects.filter(admins_pk=user_owner)
