# сериализаторы используются для преобразования данных между форматами, такими как JSON
# Для взаимодействия с API
from rest_framework import serializers
from .models import Task, UserTask

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

        extra_kwargs = {
            # указывем какие поля не обязательные
            'image': {'required': False},
            'solution': {'required': False},
            'answer': {'required': False},
        }
# делаем проверку на 4-х значное число в № задания(number)
    def validate_number(self, value):
        if value < 1000 or value > 9999:
            raise serializers.ValidationError('The number must be a 4-digit integer.')
        return value

# сериализатор для модели UserTask, где пользователь может добавлять свое решение через Api
class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = ['user', 'task', 'answer_user', 'solution_user']
