from django.urls import path
from .views import (
    HomeView, TodoListView, TodoListDetailView, TodoListDeleteView, 
    TodoListEditView, TodoDeleteView, TodoEditView
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("todo-lists", TodoListView.as_view(), name="todo_lists"),
    path("todo-lists/<int:id>", TodoListDetailView.as_view(), name="todo_list_detail"),
    path("todo-lists/<int:id>/delete", TodoListDeleteView.as_view(), name="todo_list_delete"),
    path("todo-lists/<int:id>/edit", TodoListEditView.as_view(), name="todo_list_edit"),
    path("todos/<int:id>/delete", TodoDeleteView.as_view(), name="todo_delete"),
    path("todos/<int:id>/edit", TodoEditView.as_view(), name="todo_edit"),
]