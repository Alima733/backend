from django.urls import path
from .views import get_movies, get_movie_by_id

urlpatterns = [
    path('movies/', get_movies),
    path('movies/<int:id>/', get_movie_by_id),
]