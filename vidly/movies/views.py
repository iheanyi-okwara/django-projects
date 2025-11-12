from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    # SELECT * FROM movies_movie
    # output = ', '.join([m.title for m in movies]) # this formats the result as a string
    # Movie.objects.filter(release_year=1984)
    # SELECT * FROM movies_movie WHERE
    # Movie.objects.get(id=1)
    # return HttpResponse(output)
    return render(request, 'movies/index.html', {'movies': movies})

# Note: Other things you can do with Database Abstraction API
    # Movie.objects.all()
    # SELECT * FROM movies_movie
    # Movie.objects.filter(release_year=1984)
    # SELECT * FROM movies_movie WHERE
    # Movie.objects.get(id=1)
    # return HttpResponse(output)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
