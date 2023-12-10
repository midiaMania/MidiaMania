from django.shortcuts import render, get_object_or_404
from .models import Category, Game


def games_by_category(request):
    context = {
        'games_by_categories': Category.objects.filter(game__isnull=False).distinct()
    }

    return render(request, "games/games_by_category.html", context)


def game_details(request, slug):
    game = get_object_or_404(Game, slug=slug)
    
    context = {
        'game': game
    }
    
    return render(request, "games/game_details.html", context)
