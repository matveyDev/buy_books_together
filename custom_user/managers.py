from django.contrib.auth.base_user import BaseUserManager
from rest_framework.authtoken.models import Token

from .logic import values_exists


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, subscriber, username=None, **extra_fields):
        if values_exists(email, username):
            email = self.normalize_email(email)
        else:
            raise ValueError('E-mail и логин обязателены!')

        user = self.model(
            email=email,
            is_active=True,
            is_staff=is_staff,
            subscriber=False,
            is_superuser=is_superuser,
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        new_token = Token.objects.create(user=user)
        return user

    def create_user(self, email, password, username, **extra_fields):
        return self._create_user(email, password, False, False, False, username, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, True, **extra_fields)