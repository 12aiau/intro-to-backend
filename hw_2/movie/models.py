from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    author = models.CharField(max_length=200)
    duration = models.IntegerField()

    def __str__(self):
        return self.title
