from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserTaskListView, UserTaskDetailView

# Создание маршрутизатора
# DefaultRouter автоматически создает маршруты для всех стандартных действий в TaskViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet,  basename='tasks')

urlpatterns = [
    path('', include(router.urls)), # подключения через router  задач

#а здесь уже подключаем задачи непосредственно для каждого пользователя
    path('user/tasks/', UserTaskListView.as_view(), name='user-task-list'),
    path('user/tasks/<int:pk>/', UserTaskDetailView.as_view(), name='user-task-detail'),
]
