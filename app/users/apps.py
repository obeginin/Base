from django.apps import AppConfig
#import users.signals
import os
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        os.system('python /users/signals.py')
        import signals # Подключаем файл с сигналами