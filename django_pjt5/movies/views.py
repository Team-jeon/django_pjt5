from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Genre
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)

def detail_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail_movie.html', context)
