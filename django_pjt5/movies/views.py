from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Genre
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from django.http import JsonResponse
from django.core.paginator import Paginator
import random

# Create your views here.
def index(request):
    movies = Movie.objects.all()

    # paginator
    paginator = Paginator(movies, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 추천
    genres = Genre.objects.values('name')
    # 유저가 좋아하는 장르에서 우선뽑기(만약 좋아하는 장르가 여러개라면 //n개 뽑기)
    # 유저가 좋아하는 장르가 없다면?
    # 영화 랜덤추천
    like_genres = request.user.like_genres
    recomandedMovies = []
    id_arr = []
    for movie in movies:
        id_arr.append(movie.id)
    id_set = random.sample(id_arr, 10)
    for id_ in id_arr:
        recomandedMovies.append(Movie.objects.get(id=id_))

    context = {
        'movies' : movies,
        'page_obj' : page_obj,
        'recomandedMovies' :recomandedMovies,
    }
    return render(request, 'movies/index.html', context)

def detail_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail_movie.html', context)

# @login_required
def like(request, movie_id):
    user = request.user 
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if movie.users_like_movie.filter(pk=user.pk).exists():
        movie.users_like_movie.remove(user)
        status = False
    else:
        movie.users_like_movie.add(user)
        status = True

    context = {
        'status': status,
        'count': movie.users_like_movie.count(),
    }

    return JsonResponse(context)

