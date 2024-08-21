# tasks/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task, UserTask
from users.models import User

# данный сигнал обрабатывает событие когда добавляется новая задача
# она назначается всем пользователям

@receiver(post_save, sender=Task)
def assign_task_to_all_users(sender, instance, **kwargs):
    if kwargs.get('created', False):  # Проверьте, что задача была только что создана
        users = User.objects.all()
        for user in users:
            UserTask.objects.get_or_create(user=user, task=instance)