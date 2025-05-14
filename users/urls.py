# users/urls.py
from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path('', UserList.as_view(), name='user-list'),  # URL для списка пользователей
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),  # URL для деталей пользователя по ID
]