from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "Пользоватеddль"
        verbose_name_plural = "Пользователи"