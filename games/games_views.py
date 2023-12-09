from django.shortcuts import render
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
    context = {
        'slug': slug,
        'title': 'Marvel\'s Spider-Man: Miles Morales',
        'img': 'games/images/4.jpg',
        'publisher': 'Sony Interactive Entertainment',
        'developer': 'Insomniac Games, Nixxes Software',
        'platform': 'PS4, PS5',
        'rating': 12,
        'about': 'Na aventura mais recente do universo de Marvel\'s Spider-Man, o adolescente Miles Morales está se adaptando à sua nova casa enquanto segue os passos de seu mentor, Peter Parker, para se tornar um novo Spider-Man. Mas uma violenta disputa de forças ameaça destruir seu novo lar e faz o aspirante a herói perceber que com grandes poderes também vêm grandes responsabilidades. Para salvar a Nova York da Marvel, Miles precisa reconhecer e assumir o título de Spider-Man.',
        'release_date': 2020,
        'price': "{:,.2f}".format(170).replace('.', ','),
        'categories': ['Ação', 'Aventura']
    }

    return render(request, "games/game_details.html", context)
