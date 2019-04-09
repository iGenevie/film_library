from django.urls import path
from . import views


urlpatterns = [
    path('', views.users_list, name='users_list'),
    path('films/<int:pk>/', views.films_list, name='films_list'),
    path('user/new/', views.user_new, name='user_new'),
    path('films/<int:user_pk>/new/', views.film_new, name='film_new'),
]
