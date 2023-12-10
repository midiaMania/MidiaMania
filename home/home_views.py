from django.shortcuts import render
from movies.models import Movie
from games.models import Game
from musics.models import Music

def error404(request, exception):
    return render(request, '404.html', status=404)

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
