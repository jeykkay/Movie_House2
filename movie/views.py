from django.shortcuts import render
from django.views.generic.base import View

from movie.models import Movie


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all().order_by('id')
        return render(request, 'movie_list.html', {'movies': movies, 'title': 'MOVIE HOUSE'})
