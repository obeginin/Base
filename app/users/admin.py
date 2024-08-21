from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from tasks.models import UserTask

'''
class UserTaskInline(admin.TabularInline):
    model = UserTask
    extra = 0  # Убирает пустые строки для новых задач
'''
# Отображение пользователей в Админке (users)
class MyUserAdmin(BaseUserAdmin):
# Поля, отображаемые в списке пользователей в админке
    list_display = ('login', 'last_name', 'first_name', 'email', 'phone_number', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'last_name') # фильтры с правой стороны
    #inlines = [UserTaskInline]  # Добавляем связанные задачи в админку пользователей

# Поля, доступные для редактирования в форме добавления и редактирования
    fieldsets = (
        ('Личная информция', {'fields': ('first_name', 'last_name')}),
        (None, {'fields': ('email', 'password')}),
        ('Разрешения', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        #('Разрешения', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        #('Даты', {'fields': ('last_login')}),
    )

# add_fieldsets Определяет поля для формы добавления нового пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'email', 'phone_number', 'last_name', 'first_name', 'password1', 'password2', 'is_staff'),
        }),
    )

# search_fields: Определяет, по каким полям будет осуществляться поиск в списке пользователей.
    search_fields = ('login', 'email', 'first_name', 'last_name')
    ordering = ('email',)

# filter_horizontal: Определяет, какие поля будут отображаться с горизонтальными фильтрами (например, группы и разрешения).
    filter_horizontal = ('groups', 'user_permissions')

# Регистрация модели и ее администратора
admin.site.register(User, MyUserAdmin)

