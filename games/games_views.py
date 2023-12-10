from django.shortcuts import render, get_object_or_404
from .models import Category, Game


def games_by_category(request):
    categories = Category.objects.all()
    games_by_category = {}
    for category in categories:
        games = category.game_set.all()
        games_list = []
        for game in games:
            games_list.append({
                'name': game.title,
                'price': "{:,.2f}".format(game.price).replace('.', ','),
                'img': game.image.url,
                'slug': game.slug
        })
        games_by_category[category.name] = games_list

    context = {
        'games_by_category': games_by_category
    }

    return render(request, "games/games_by_category.html", context)


def game_details(request, slug):
    game = get_object_or_404(Game, slug=slug)
    
    context = {
        'game': game
    }
    
    return render(request, "games/game_details.html", context)
