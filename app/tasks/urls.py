from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Создание маршрутизатора
# DefaultRouter автоматически создает маршруты для всех стандартных действий в TaskViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
