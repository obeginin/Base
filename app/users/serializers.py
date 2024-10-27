from rest_framework import serializers # модуль сериализаторов
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password # валидатор для проверки пароля

# получаем модель пользоваеля, указанную в настройках
User = get_user_model()

# часть сериализатора отвечающая за регистрацию и аутентификацию
class UserSerializer(serializers.ModelSerializer):
# required поле обязательно для заполнения
# validators проверяет пароль на соответствие стандартам безопасности
    # style={'input_type': 'password'} атрибут для скрытия пароля
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password], style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})  # используется для проверки повторного ввода пароля.
    class Meta:
# указываем модель для кого задем сериализатор
# и перечисляем поля для их включения
        model = User
        fields = ['id', 'login', 'email', 'phone_number', 'last_name', 'first_name', 'password', 'password2']

# Проверяет совпадение двух паролей
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})
        return attrs


# метод  создаёт нового пользователя на основе данных, которые были проверены и валидированы сериализаторо
    def create(self, validated_data):
        #print(validated_data)
        user = User.objects.create_user(
            
            login = validated_data['login'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            last_name=validated_data['last_name'],
            first_name=validated_data['first_name'],
            password=validated_data['password']
        )
        return user

#  сериализатор для аутентификации
class LoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        user = authenticate(login=data['login'], password=data['password']) # Используем login вместо username
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные.")


