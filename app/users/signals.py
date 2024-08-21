from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from tasks.models import Task, UserTask #

User = get_user_model() # Сигнал, который срабатывает после создания пользователя

# данный сигнал обрабатывает событие когда добавляется новый пользователь
# для его назначаются все задачи из модели tasks
@receiver(post_save, sender=User)
def assign_tasks_to_new_user(sender, instance, created, **kwargs):
    if created: # проверяем, что пользователь создан
        tasks = Task.objects.all() # получаем все задания из таблицы
        for task in tasks:
            UserTask.objects.create(user=instance, task=task)
