from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from admins.managers import AdminsManager


class Admins(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    bot_id = models.BigIntegerField(unique=True)
    contact = models.CharField(max_length=13)
    username = models.CharField(
        max_length=150,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator]
    )

    USERNAME_FIELD = 'bot_id'
    REQUIRED_FIELDS = ['contact', 'email']

    objects = AdminsManager()

    def __str__(self):
        return str(self.bot_id)
