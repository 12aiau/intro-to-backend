from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie

def get_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movies': movies})

def get_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movie/movie_detail.html', {'movie': movie})