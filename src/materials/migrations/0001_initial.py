# Generated by Django 4.1.4 on 2022-12-29 16:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import materials.models
import materials.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, validators=[materials.validators.validate_folder_name_length, materials.validators.validate_name], verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталоги',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_private', models.BooleanField(default=0, verbose_name='Ограниченный доступ')),
                ('name', models.CharField(max_length=30, validators=[materials.validators.validate_document_name_length, materials.validators.validate_name], verbose_name='Название')),
                ('disk_path', models.FileField(upload_to=materials.models.catalog_path, validators=[materials.validators.validate_file_size, django.core.validators.FileExtensionValidator(['docx', 'xls', 'xlsx', 'pdf', 'pptx', 'ppt', 'pptm', 'png', 'jpeg', 'jpg'], message='Данный формат файла не поддерживается')], verbose_name='Файл')),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.catalog', verbose_name='Каталог')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
    ]
