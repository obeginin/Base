from django.contrib import admin
from django.urls import path, include

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
]
