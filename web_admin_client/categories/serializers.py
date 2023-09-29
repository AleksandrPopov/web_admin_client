from rest_framework import serializers

from categories.models import Categories


class CategoriesSerializer(serializers.ModelSerializer):
    admins_pk = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Categories
        fields = ('id', 'name', 'admins_pk')
