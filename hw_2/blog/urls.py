from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.get_articles, name='get_articles'),
    path('articles/<int:id>/', views.get_article, name='get_article'),
]