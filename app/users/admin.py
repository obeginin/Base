from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class MyUserAdmin(BaseUserAdmin):
# Поля, отображаемые в списке пользователей в админке
    list_display = ('login', 'last_name', 'first_name', 'email', 'phone_number', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'last_name') # фильтры с правой стороны

# Поля, доступные для редактирования в форме добавления и редактирования
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Личная информция', {'fields': ('first_name', 'last_name')}),
        ('Разрешения', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Даты', {'fields': ('last_login', 'date_joined')}),
    )

# add_fieldsets Определяет поля для формы добавления нового пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'email', 'last_name', 'first_name', 'password1', 'password2', 'is_staff'),
        }),
    )

# search_fields: Определяет, по каким полям будет осуществляться поиск в списке пользователей.
    search_fields = ('login', 'email', 'first_name', 'last_name')
    ordering = ('email',)

# filter_horizontal: Определяет, какие поля будут отображаться с горизонтальными фильтрами (например, группы и разрешения).
    filter_horizontal = ('groups', 'user_permissions')

# Регистрация модели и ее администратора
admin.site.register(User, MyUserAdmin)