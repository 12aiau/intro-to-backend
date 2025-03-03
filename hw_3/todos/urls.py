from django.urls import path
from .views import index, todo_detail, todo_create, todo_delete

urlpatterns = [
    path('todos/', index, name='index'),
    path('todos/<int:id>', todo_detail, name='todo_detail'),
    path('create/', todo_create, name='todo_create'),
    path('todos/<int:id>/delete', todo_delete, name='todo_delete'),
]
