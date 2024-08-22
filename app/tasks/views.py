# Представления (логика работы приложения)
from rest_framework import viewsets # предоставляет стандартные действия для CRUD-операций (Create, Read, Update, Delete)
from rest_framework import generics, permissions
from .models import Task, UserTask
from .serializers import TaskSerializer, UserTaskSerializer # мпорт сериализатора

# TaskViewSet предоставляет стандартные методы для обработки запросов к API.
# list: Получить список всех объектов.
# create: Создать новый объект.
# retrieve: Получить конкретный объект по его идентификатору.
# update: Обновить существующий объект.
# partial_update: Частично обновить объект.
# destroy: Удалить объект.

# ModelViewSet автоматически связывается с URL-адресами, если вы используете маршрутизатор в вашем urls.pyS
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all() # берем все аобъекты нашей модели Task
    serializer_class = TaskSerializer

# добавляем логику для получения и редактирования задач пользователя
class UserTaskListView(generics.ListCreateAPIView):
    serializer_class = UserTaskSerializer
    permission_classes = [permissions.IsAuthenticated] # Доступ только для авторизованных пользователей

    def get_queryset(self):
        # Возвращаем задачи только для текущего пользователя
        return UserTask.objects.filter(user=self.request.user)

class UserTaskDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserTaskSerializer
    permission_classes = [permissions.IsAuthenticated]  # Доступ только для авторизованных пользователей

    def get_queryset(self):
        # Возвращаем конкретную задачу, которая принадлежит текущему пользователю
        return UserTask.objects.filter(user=self.request.user)