from django.shortcuts import render
from movies.models import Movie
from games.models import Game
from musics.models import Music

def error404(request, exception):
    return render(request, '404.html', status=404)

def home(request):
    movies = Movie.objects.all()[:10]
    musics = Music.objects.all()[:10]
    games = Game.objects.all()[:10]

    movies_list=[]
    musics_list=[]
    games_list=[]
    
    for movie in movies:
            movies_list.append({
                'name': movie.title,
                'price': "{:,.2f}".format(movie.price).replace('.', ','),
                'img': movie.img.url,
                'slug': movie.slug
        })

    for game in games:
            games_list.append({
                'name': game.title,
                'price': "{:,.2f}".format(game.price).replace('.', ','),
                'img': game.img.url,
                'slug': game.slug
        })
            
    for music in musics:
            musics_list.append({
                'name': music.name,
                'price': "{:,.2f}".format(music.price).replace('.', ','),
                'img': music.img.url,
                'slug': music.slug
        })
            
    context = {
        'movies': movies_list,
        'musics': musics_list,
        'games': games_list
    }
    return render(request, "home/home.html", context)
