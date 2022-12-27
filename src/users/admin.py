from django.conf import settings
from django.contrib import admin
from django.contrib.admin import StackedInline
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from staff.models import Employee
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class ProfileInline(StackedInline):
    model = Employee


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ('id', 'email', 'is_staff', 'is_active', 'date_joined', 'last_login',)
    list_display_links = ('id', 'email',)
    list_filter = ('is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('id',)
    inlines = [ProfileInline]

    fieldsets = (
        ('УЧЕТНАЯ ЗАПИСЬ', {'fields': ('email', 'password', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'is_staff', 'is_active')}
         ),
    )

    def save_model(self, request, obj, form, change):
        if not change and (not form.cleaned_data['password1'] or not obj.has_usable_password()):
            password = get_random_string(length=12)
            obj.set_password(password)
            send_mail(
                subject='Корпоративная база знаний',
                message='Вы зарегистрированы в системе Корпоративной базы знаний\n'
                        f'Ваш логин - {obj.email}, пароль - {password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[obj.email],
            )

        super().save_model(request, obj, form, change)


admin.site.unregister(Group)
