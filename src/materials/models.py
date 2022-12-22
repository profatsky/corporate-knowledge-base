from os.path import splitext

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import validate_document_name_length, validate_name, validate_folder_name_length, validate_file_size


def catalog_path(instance, filename):
    return f"{instance.catalog.name}/{instance.name}{splitext(filename)[-1]}"


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
                ['docx', 'xls', 'pdf', 'pptx', 'ppt', 'pptm', 'png', 'jpeg'],
                message=_('File Extension is not supported')
            )
        ],
        verbose_name='Файл'
    )

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return str(self.name)


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
        return str(self.name)
