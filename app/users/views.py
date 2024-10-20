from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import LoginSerializer
from django.contrib.auth import authenticate

# регистрация
# CreateAPIView автоматически создает пользователя на основе сериализатора и отправляет отве
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer


# create() обрабатывает запрос, валидирует данные и возвращает ответ с сообщением об успешной регистрации
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializer.data,
            "message": "Пользователь успешно зарегистрирован."
        }, status=status.HTTP_201_CREATED)


# Аутентификация
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "message": "Вы успешно вошли в систему."
        }, status=status.HTTP_200_OK)