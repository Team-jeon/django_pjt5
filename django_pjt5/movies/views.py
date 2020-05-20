from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Genre
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from django.core.paginator import Paginator

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'movies' : movies,
        'page_obj' : page_obj,
    }
    return render(request, 'movies/index.html', context)

def detail_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail_movie.html', context)
