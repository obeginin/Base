from django.urls import path
from .views import RegisterView, LoginView
from .views import LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api-token-auth/', LoginView.as_view(), name='api_token_auth'),
]