from django.test import TestCase
from ..serializers import UserSerializer
from django.contrib.auth import get_user_model

# тест на создание пользователя, для проверки сериализатора
User = get_user_model()

class UserSerializerTest(TestCase):
    def test_create_user(self):
        data = {
            'login': 'John1980',
            'email': 'johndoe@example.com',
            'phone_number': ' + 123456789',
            'last_name': 'Doe',
            'first_name': 'John',
            'password': 'SecureP@ss123'
        }
        print(f"Данные для теста: {data}")
        serializer = UserSerializer(data=data) # содется экземпляр сериаизатоора с данными
        if not serializer.is_valid():
            print(serializer.errors)

        self.assertTrue(serializer.is_valid()) # проверяет прошли ли мы проверку на валидацию
        user = serializer.save()    # сохраняет данные из сериализатора и создаёт новый объект
        self.assertEqual(user.login, 'johndoe') # Проверяем, что login сохранен корректно
        self.assertEqual(user.email, 'johndoe@example.com')  # Проверяет, что email, сохраненный в базе данных, совпадает с ожидаемым значением.
        self.assertTrue(user.check_password('SecureP@ss123'))   # Проверяет, что пароль пользователя был сохранен корректно и совпадает с переданным значением.