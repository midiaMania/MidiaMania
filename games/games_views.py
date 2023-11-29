from django.shortcuts import render


def games_by_category(request):
    context = {
        'fps_games': [
            {
                'name': "Doom",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/2.jpg",
                'slug': "fps"
            },
            {
                'name': "Watch Dogs",
                'price': "{:,.2f}".format(40).replace('.', ','),
                'img': "games/images/3.jpg",
                'slug': "fps"
            },
            {
                'name': "Red Alert 3",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/6.jpg",
                'slug': "fps"
            },
            {
                'name': "Doom",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/2.jpg",
                'slug': "fps"
            },
            {
                'name': "Watch Dogs",
                'price': "{:,.2f}".format(40).replace('.', ','),
                'img': "games/images/3.jpg",
                'slug': "fps"
            },
            {
                'name': "Red Alert 3",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/6.jpg",
                'slug': "fps"
            },
            {
                'name': "Doom",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/2.jpg",
                'slug': "fps"
            },
            {
                'name': "Watch Dogs",
                'price': "{:,.2f}".format(40).replace('.', ','),
                'img': "games/images/3.jpg",
                'slug': "fps"
            },
            {
                'name': "Red Alert 3",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/6.jpg",
                'slug': "fps"
            },
        ],

        'fantasy_games': [
            {
                'name': "Zelda",
                'price': "{:,.2f}".format(140).replace('.', ','),
                'img': "games/images/1.jpeg",
                'slug': "fantasy"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg",
                'slug': "fantasy"
            },
            {
                'name': "Assassin's Creed",
                'price': "{:,.2f}".format(50).replace('.', ','),
                'img': "games/images/5.jpg",
                'slug': "fantasy"
            },
            {
                'name': "Zelda",
                'price': "{:,.2f}".format(140).replace('.', ','),
                'img': "games/images/1.jpeg",
                'slug': "fantasy"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg",
                'slug': "fantasy"
            },
            {
                'name': "Assassin's Creed",
                'price': "{:,.2f}".format(50).replace('.', ','),
                'img': "games/images/5.jpg",
                'slug': "fantasy"
            },
            {
                'name': "Zelda",
                'price': "{:,.2f}".format(140).replace('.', ','),
                'img': "games/images/1.jpeg",
                'slug': "fantasy"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg",
                'slug': "fantasy"
            },
            {
                'name': "Assassin's Creed",
                'price': "{:,.2f}".format(50).replace('.', ','),
                'img': "games/images/5.jpg",
                'slug': "fantasy"
            },
        ],

        'hero_games': [
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg",
                'slug': "hero"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg",
                'slug': "hero"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg",
                'slug': "hero"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg",
                'slug': "hero"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg",
                'slug': "hero"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg",
                'slug': "hero"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg",
                'slug': "hero"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg",
                'slug': "hero"
            },
        ],
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
