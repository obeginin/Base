# users/models.py в данном файле описывем модель для хранения информации о пользователях в БД
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
# AbstractBaseUser: set_password


# Класс для управления созданием пользователей.

class UserManager(BaseUserManager):
    # Функция для создания обычного ользователя (стандартная в Django).
    def create_user(self, login, password=None, **extra_fields): # логин и пароль обятельные аргументы, **extra_fields означает что могут быть переданы и другие аргументы
        if not login:
            raise ValueError('Логин должен быть указан')
        user = self.model(login=login,  **extra_fields) # Создает пользователя с указанным email и дополнительными полями
        #email = self.normalize_email(email)  # приводит email к стандартному виду, делает его строчным)
        user.set_password(password) # Устанавливает пароль (хеширует его). даный метод set_password() принадлеит классу AbstractBaseUser
        user.save(using=self._db) # С помощью метода save() Сохраняеем экземпляр пользователя в базе данных.
        return user


# Функция для создания суперпользователя (стандартная в Django). ОН так же вызывает метод create_user()
# для создания суперпользователя в комадно срое вводим: python manage.py createsuperuser
    def create_superuser(self, login, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(login, password, **extra_fields)



# Основная модель для пользователя.
class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=30, unique=True, verbose_name='Логин')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия') # Фамилия
    first_name = models.CharField(max_length=255, verbose_name='Имя') # Имя
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Мобильный телефон')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    is_active = models.BooleanField(default=True) # проверка активности польовтеля
    is_staff = models.BooleanField(default=False, verbose_name='админ') # является ли пользователь сотрудником (имеет доступ к административному интерфейсу).

    objects = UserManager()

# USERNAME_FIELD Django использует login как имя пользователя для аутентификации.
    USERNAME_FIELD = 'login'
# REQUIRED_FIELDS Эти поля являются обязательными при создании суперпользователя через команду createsuperuser .
    REQUIRED_FIELDS = ['first_name', 'last_name']

# Метод __str__ возвращающий строковое представление объекта. В данном случае возвращает login пользователя,
# что полезно для отображения пользователя в административной панели Django
    def __str__(self):
        return self.login

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='myuser_groups',  # Уникальное имя для предотвращения конфликта
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='myuser_permissions',  # Уникальное имя для предотвращения конфликта
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )