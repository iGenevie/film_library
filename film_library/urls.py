from django.urls import path
from . import views


urlpatterns = [
    path('', views.users_list, name='users_list'),
    path('films/<int:pk>/', views.films_list, name='films_list'),
]
