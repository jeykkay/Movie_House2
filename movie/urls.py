from django.urls import path

from movie.views import MoviesView


urlpatterns = [
    path('', MoviesView.as_view(), name='movie_list'),
]
