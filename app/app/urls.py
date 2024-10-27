from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token



# GET /api/tasks/: Получить список всех задач.
# POST /api/tasks/: Создать новую задачу.
# GET /api/tasks/{id}/: Получить конкретную задачу по ID.
# PUT /api/tasks/{id}/: Обновить задачу по ID.
# PATCH /api/tasks/{id}/: Частично обновить задачу по ID.
# DELETE /api/tasks/{id}/: Удалить задачу по ID.

urlpatterns = [
    path('admin/', admin.site.urls),     # Стандартный URL для административного интерфейса
    path('api/', include('tasks.urls')),  # Добавление маршрутов API для задач
    path('api/', include('users.urls')),  # подключаем маршруты API для users
    path('api/token/', obtain_auth_token, name='api_token_auth'),  # для получения токена
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
