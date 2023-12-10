from django.shortcuts import render
from django.db.models import Q
from movies.models import Movie
from games.models import Game
from musics.models import Music

def error404(request, exception):
    return render(request, '404.html', status=404)

def search(request):
    query = request.GET.get('q')
    
    if query:
        results = list(
            Movie.objects.filter(Q(title__icontains=query) | Q(synopsis__icontains=query))[:10]
        ) + list(
            Game.objects.filter(Q(title__icontains=query) | Q(about__icontains=query))[:10]
        ) + list(
            Music.objects.filter(Q(title__icontains=query) | Q(artist__icontains=query))[:10]
        )
    else:
        results = []
    
    context = {
        'query': query,
        'results': results
    }
    
    return render(request, 'home/search.html', context)

def home(request):
    movies = Movie.objects.all()[:20]
    musics = Music.objects.all()[:20]
    games = Game.objects.all()[:20]
            
    context = {
        'movies': movies,
        'musics': musics,
        'games': games
    }
    
    return render(request, "home/home.html", context)
