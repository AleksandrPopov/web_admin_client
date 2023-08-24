from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AdminsForm
from .models import *
from django.contrib.auth.models import User, Group


class AuthAdmin(UserAdmin):
    form = AdminsForm
    add_form = AdminsForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "bot_id", "email", "contact", "password1", "password2"),
            },
        ),
    )

admin.site.unregister(Group)
admin.site.register(Admins, AuthAdmin)
