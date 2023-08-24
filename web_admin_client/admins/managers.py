from django.contrib.auth.base_user import BaseUserManager


class AdminsManager(BaseUserManager):
    def create_user(self, email, contact, bot_id, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            contact=contact,
            bot_id=bot_id,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, contact, bot_id, password=None):
        user = self.create_user(
            email=email,
            password=password,
            contact=contact,
            bot_id=bot_id,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return super().get_by_natural_key(username)

