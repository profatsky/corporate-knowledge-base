from os.path import splitext

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import validate_document_name_length, validate_name, validate_folder_name_length, validate_file_size


def catalog_path(instance, filename):
    return f"{instance.catalog.name}/{instance.name.split('.')[:-1]}{splitext(filename)[-1]}"


class Document(models.Model):
    catalog = models.ForeignKey('Catalog', on_delete=models.CASCADE, verbose_name='Каталог')
    is_private = models.BooleanField(default=0, verbose_name='Ограниченный доступ')
    name = models.CharField(
        max_length=30,
        validators=[validate_document_name_length, validate_name],
        verbose_name='Название'
    )
    disk_path = models.FileField(
        upload_to=catalog_path,
        validators=[
            validate_file_size,
            FileExtensionValidator(
                ['docx', 'xls', 'xlsx', 'pdf', 'pptx', 'ppt', 'pptm', 'png', 'jpeg', 'jpg'],
                message=_('Данный формат файла не поддерживается')
            )
        ],
        verbose_name='Файл'
    )

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.name = f"{self.name}.{self.disk_path.name.split('.')[-1]}"
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class Catalog(models.Model):
    name = models.CharField(
        max_length=20,
        validators=[validate_folder_name_length, validate_name],
        unique=True,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    def __str__(self):
        return self.name
