from django.shortcuts import render

def movies_by_category(request):
    return render(request, "movies/movies_by_category.html")


def movie_details(request, slug):
    context = {
        'slug': slug,
        'title': 'Avengers: Endgame',
        'img': 'movies/images/4.jpg',
        'release_date': 2019,
        'running_time': 181,
        'value': 4500,
        'categories': ['Ação', 'Aventura', 'Fantasia']    
    }
    
    return render(request, "movies/movie_details.html", context)
