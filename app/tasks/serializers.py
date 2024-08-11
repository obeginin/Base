# сериализаторы используются для преобразования данных между форматами, такими как JSON
# Для взаимодействия с API
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'