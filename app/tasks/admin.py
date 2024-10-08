from django.contrib import admin
from .models import Task, UserTask


class TaskAdmin(admin.ModelAdmin):
    # Поля, отображаемые в списке пользователей в админке
    list_display = ('category', 'resour', 'number', 'image', 'solution', 'answer')  # Поля, которые будут отображаться в списке задач
    search_fields = ('number', 'resour')  # Поля для поиска
    list_filter = ('category', 'resour', 'number', )  # Фильтрация по названию задачи

admin.site.register(Task, TaskAdmin)

class MyUserTaskAdmin(admin.ModelAdmin):
# Поля, отображаемые в списке пользователей в админке
    list_display = ('user',)

admin.site.register(UserTask)

'''

@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Поля, которые будут отображаться в списке
    search_fields = ('name',)  # Поля для поиска в админке


admin.site.register(Task)

@admin.register(Task)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    '''

