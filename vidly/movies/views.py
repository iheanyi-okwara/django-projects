from django.http import HttpResponse
from django.shortcuts import render
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
