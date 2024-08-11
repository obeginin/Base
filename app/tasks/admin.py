from django.contrib import admin
from .models import Task
admin.site.register(Task)

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

