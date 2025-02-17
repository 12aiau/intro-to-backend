from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.get_movies, name='get_movies'),
    path('movies/<int:id>/', views.get_movie, name='get_movie'),
]