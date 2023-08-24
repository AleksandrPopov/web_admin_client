from django.db import models

from admins.models import Admins


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    admins_pk = models.ForeignKey(Admins, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'admins_pk')
