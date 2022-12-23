from django.conf import settings
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Сотрудник')
    fio = models.CharField(max_length=256, verbose_name='ФИО')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name='Отдел')
    birth_date = models.DateField(verbose_name='Дата рождения')
    extended_access = models.BooleanField(default=0, verbose_name='Расширенный доступ')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return str(self.user)
