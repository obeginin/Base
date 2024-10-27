# users/signals.py
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from app.tasks.models import Task, UserTask #

User = get_user_model() # Сигнал, который срабатывает после создания пользователя

# данный сигнал обрабатывает событие когда добавляется новый пользователь
# для его назначаются все задачи из модели tasks
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created: # проверяем, что пользователь создан
        Token.objects.create(user=instance) # Получаем токен для пользователя
        tasks = Task.objects.all() # получаем все задания из таблицы
        for task in tasks:
            UserTask.objects.create(user=instance, task=task)
