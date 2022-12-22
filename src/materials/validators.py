from string import ascii_letters, digits

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_document_name_length(value: str):
    if not 7 <= len(value) <= 30:
        raise ValidationError(
            _('Длина названия документа должна быть не менее 7 и не более 30 символов'),
            params={'value': value}
        )
    return value


def validate_folder_name_length(value: str):
    if not 5 <= len(value) <= 20:
        raise ValidationError(
            _('Длина названия каталога должна быть не менее 5 и не более 20 символов'),
            params={'value': value}
        )
    return value


def validate_file_size(value):
    limit = 20971520
    if value.size > limit:
        raise ValidationError('Размер файла не должен превышать 20 МБ')
    return value


def validate_name(value: str):
    cyrillic_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    specific_letters = '№:()-_.'
    validate_letters = ascii_letters + digits + cyrillic_letters + specific_letters

    if set(value.lower()) - set(validate_letters):
        raise ValidationError(
            _('Разрешенные символы кириллица, латиница, цифры, спецсимволы №:()-_'),
            params={'value': value}
        )
    return value
