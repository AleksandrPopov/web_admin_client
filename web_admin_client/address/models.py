from django.db import models

from admins.models import Admins


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    house = models.CharField(max_length=64)
    admins_pk = models.ForeignKey(Admins, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('city', 'street', 'house', 'admins_pk')

