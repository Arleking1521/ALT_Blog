from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(verbose_name='Имя')
    surname = models.CharField(verbose_name='Фамилия')
    phone = models.CharField(verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта', unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=128)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'surname', 'password']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # уникальное имя для обратной ссылки
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # уникальное имя для обратной ссылки
        blank=True
    )

    def __str__(self):
        return f"{self.name} {self.surname} {self.email}"
