from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
    
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    due_date = models.DateField()
    status = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="todos")

    def __str__(self):
        return self.title