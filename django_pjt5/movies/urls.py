from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail_movie, name='detail_movie'),
]
