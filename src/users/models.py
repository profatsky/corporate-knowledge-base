from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(blank=True, unique=True, verbose_name='Email')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.password:
            password = User.objects.make_random_password()
            self._password = password
            self.password = make_password(password)
            send_mail(
                subject='Корпоративная база знаний',
                message='Вы зарегистрированы в системе Корпоративной базы знаний\n'
                        f'Ваш логин - {self.email}, пароль - {self._password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.email],
            )
        super().save()

    def __str__(self):
        return self.email
