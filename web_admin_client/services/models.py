from django.db import models

from admins.models import Admins
from categories.models import Categories


class Services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    time = models.TimeField()
    cost = models.IntegerField()
    categories_pk = models.ForeignKey(Categories, on_delete=models.CASCADE)
    admins_pk = models.ForeignKey(Admins, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'categories_pk', 'admins_pk')
