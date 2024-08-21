# tasks/admin.py

from django.contrib import admin
from .models import Task, UserTask

#from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class TaskAdmin(admin.ModelAdmin):
    # Поля, отображаемые в списке пользователей в админке
    list_display = ('category', 'resour', 'number', 'image', 'solution', 'answer')  # Поля, которые будут отображаться в списке задач
    search_fields = ('number', 'resour')  # Поля для поиска
    list_filter = ('category', 'resour', 'number', )  # Фильтрация по названию задачи


admin.site.register(Task, TaskAdmin)


class MyUserTaskAdmin(admin.ModelAdmin):
# Поля, отображаемые в списке пользователей в админке
    list_display = ('user',)

admin.site.register(UserTask, MyUserTaskAdmin)
'''
# Отображение задач-пользователей в Админке ()
class MyUserTaskAdmin(BaseUserAdmin):
# Поля, отображаемые в списке пользователей в админке
    #list_display = ('user_login', 'tasks_number', 'tasks_image', 'completed', 'answer_user', 'tasks_answer', 'solution_user', 'tasks_solution')
    list_display = ('user',)
    #list_filter = ('user_login') # фильтры с правой стороны
    #inlines = [UserTaskInline]  # Добавляем связанные задачи в админку пользователей

'''


