from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.shortcuts import reverse
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True, verbose_name='Email')
    username = models.CharField(max_length=50, unique=True, null=True, verbose_name='Логин')
    full_name = models.CharField(max_length=250, blank=True, verbose_name='ФИО')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    subscriber = models.BooleanField(default=False, verbose_name='Подписан на рассылку')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    age = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг пользователя')

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = CustomUserManager()

    def __str__(self):
        return str(self.full_name)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-id']