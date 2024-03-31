from django.shortcuts import render
from django.views.generic import ListView

from movie.models import Movie


class MoviesView(ListView):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movie_list.html', {'movies': movies})
