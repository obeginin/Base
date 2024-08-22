from django.contrib import admin
from .models import Task, UserTask
#from app.users imp


class TaskAdmin(admin.ModelAdmin):
    # Поля, отображаемые в списке пользователей в админке
    list_display = ('category', 'resour', 'number', 'image', 'solution', 'answer')  # Поля, которые будут отображаться в списке задач
    search_fields = ('number', 'resour')  # Поля для поиска
    list_filter = ('category', 'resour', 'number', )  # Фильтрация по названию задачи

admin.site.register(Task, TaskAdmin)

class MyUserTaskAdmin(admin.ModelAdmin):
# Поля, отображаемые в списке пользователей в админке
    list_display = ('user', 'task', 'completed', 'is_answer_correct', 'answer_user', 'task_answer', 'solution_user', 'task_solution', 'task_image')
    list_filter = ('user', 'task', 'completed')
# Методы для отображения полей из связанных моделей
# указывается название модели_название поля
    def task_image(self, obj):
        return obj.task.image # возвращаем значение из модели
    task_image.short_description = 'Задание' # задаем название для подписи столбца

    def task_answer(self, obj):
        return obj.task.answer
    task_answer.short_description = 'Ответ задачи'

    def task_solution(self, obj):
        return obj.task.solution
    task_solution.short_description = 'решение'



'''
    def is_answer_correct(self, obj):
        return obj.is_answer_correct
    is_answer_correct.boolean = True  # Показывать как булев флажок
    task_solution.short_description = 'Верно'

'''

admin.site.register(UserTask, MyUserTaskAdmin)



