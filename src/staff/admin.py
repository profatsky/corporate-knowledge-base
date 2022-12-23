from django.contrib import admin

from .models import Department, Employee


class EmployeeInline(admin.TabularInline):
    extra = 1
    model = Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    inlines = [EmployeeInline]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'department', 'birth_date')
    list_display_links = ('id', 'fio',)
    search_fields = ('fio',)
