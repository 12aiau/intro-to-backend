from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

class HomeView(View):
    def get(self, request):
        return redirect("/todo-lists")

class TodoListView(View):
    def get(self, request):
        todo_lists = TodoList.objects.all()
        form = TodoListForm()
        return render(request, "todos/todo_lists.html", {"todo_lists": todo_lists, "form": form})
    
    def post(self, request):
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/todo-lists")
        return render(request, "todos/todo_lists.html", {"form": form})

class TodoListDetailView(View):
    def get(self, request, id):
        todo_list = get_object_or_404(TodoList, id=id)
        todos = todo_list.todos.all()
        form = TodoForm()
        return render(request, "todos/todo_list_detail.html", {"todo_list": todo_list, "todos": todos, "form": form})
    
    def post(self, request, id):
        todo_list = get_object_or_404(TodoList, id=id)
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_list = todo_list
            todo.save()
            return redirect(f"/todo-lists/{id}")
        return render(request, "todos/todo_list_detail.html", {"form": form})

class TodoListDeleteView(View):
    def post(self, request, id):
        todo_list = get_object_or_404(TodoList, id=id)
        todo_list.delete()
        return redirect("/todo-lists")

class TodoListEditView(View):
    def get(self, request, id):
        todo_list = get_object_or_404(TodoList, id=id)
        form = TodoListForm(instance=todo_list)
        return render(request, "todos/todo_list_edit.html", {"form": form, "todo_list": todo_list})
    
    def post(self, request, id):
        todo_list = get_object_or_404(TodoList, id=id)
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect("/todo-lists")
        return render(request, "todos/todo_list_edit.html", {"form": form, "todo_list": todo_list})

class TodoDeleteView(View):
    def post(self, request, id):
        todo = get_object_or_404(Todo, id=id)
        todo_list_id = todo.todo_list.id
        todo.delete()
        return redirect(f"/todo-lists/{todo_list_id}")

class TodoEditView(View):
    def get(self, request, id):
        todo = get_object_or_404(Todo, id=id)
        form = TodoForm(instance=todo)
        return render(request, "todos/todo_edit.html", {"form": form, "todo": todo})
    
    def post(self, request, id):
        todo = get_object_or_404(Todo, id=id)
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect(f"/todo-lists/{todo.todo_list.id}")
        return render(request, "todos/todo_edit.html", {"form": form, "todo": todo})
