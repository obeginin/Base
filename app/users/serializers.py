from rest_framework import serializers # модуль сериализаторов
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password # валидатор для проверки пароля

# получаем модель пользоваеля, указанную в настройках
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
# required поле обязательно для заполнения
# validators проверяет пароль на соответствие стандартам безопасности
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        # указываем модеель для кого задем сериализатор
        # и перечисляем поля для включения их 
        model = User
        fields = ['id', 'login', 'email', 'phone_number', 'last_name', 'first_name', 'password']

# метод  создаёт нового пользователя на основе данных, которые были проверены и валидированы сериализаторо
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(
            
            login = validated_data['login'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            last_name=validated_data['last_name'],
            first_name=validated_data['first_name'],
            password=validated_data['password']
        )
        return user