# Представления (логика работы приложения)
from rest_framework import viewsets # предоставляет стандартные действия для CRUD-операций (Create, Read, Update, Delete)
from .models import Task
from .serializers import TaskSerializer # мпорт сериализатора

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