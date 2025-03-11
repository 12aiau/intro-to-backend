from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todos/new/', views.create_todo, name='create_todo'),
    path('todos/<int:id>/delete/', views.delete_todo, name='delete_todo'),
]
