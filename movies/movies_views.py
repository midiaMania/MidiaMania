from django.shortcuts import render, get_object_or_404
from .models import Category, Movie


def movies_by_category(request):
    context = {
        'movies_by_categories': Category.objects.filter(movie__isnull=False).distinct()
    }
    
    return render(request, "movies/movies_by_category.html", context)


def movie_details(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    
    context = {
        'movie': movie
    }

    return render(request, "movies/movie_details.html", context)
