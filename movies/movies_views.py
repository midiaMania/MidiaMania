from django.shortcuts import render, get_object_or_404
from .models import Category, Movie


def movies_by_category(request):
    categories = Category.objects.all()
    movies_by_category = {}
    for category in categories:
        movies = category.movie_set.all()
        movies_list = []
        for movie in movies:
            movies_list.append({
                'name': movie.title,
                'price': "{:,.2f}".format(movie.price).replace('.', ','),
                'img': movie.img.url,
                'slug': movie.slug
        })
        movies_by_category[category.name] = movies_list

    context = {
        'movies_by_category': movies_by_category
    }
    
    return render(request, "movies/movies_by_category.html", context)


def movie_details(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    
    context = {
        'movie': movie
    }

    return render(request, "movies/movie_details.html", context)
