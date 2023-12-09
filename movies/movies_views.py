from django.shortcuts import render
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
    context = {
        'slug': slug,
        'title': 'Avengers: Endgame',
        'img': 'movies/images/4.jpg',
        'directors': 'Anthony Russo e Joe Russo',
        'rating': 12,
        'synopsis': 'Após os eventos devastadores de "Vingadores: Guerra Infinita", o universo está em ruínas devido aos esforços do Titã Louco, Thanos. Com a ajuda de aliados remanescentes, os Vingadores devem se reunir mais uma vez a fim de desfazer as ações de Thanos e restaurar a ordem no universo de uma vez por todas, não importando as consequências.',
        'release_date': 2019,
        'running_time': 181,
        'price': "{:,.2f}".format(14).replace('.', ','),
        'categories': ['Ação', 'Aventura', 'Fantasia']
    }

    return render(request, "movies/movie_details.html", context)
