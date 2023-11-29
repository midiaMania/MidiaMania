from django.shortcuts import render

def games_by_category(request):
    context = {
        'fps_games': [
            {
                'name': "Doom",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/2.jpg"
            },
            {
                'name': "Watch Dogs",
                'price': "{:,.2f}".format(40).replace('.', ','),
                'img': "games/images/3.jpg"
            },
            {
                'name': "Red Alert 3",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/6.jpg"
            },
                        {
                'name': "Doom",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/2.jpg"
            },
            {
                'name': "Watch Dogs",
                'price': "{:,.2f}".format(40).replace('.', ','),
                'img': "games/images/3.jpg"
            },
            {
                'name': "Red Alert 3",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/6.jpg"
            },
                        {
                'name': "Doom",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/2.jpg"
            },
            {
                'name': "Watch Dogs",
                'price': "{:,.2f}".format(40).replace('.', ','),
                'img': "games/images/3.jpg"
            },
            {
                'name': "Red Alert 3",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/6.jpg"
            },
        ],

        'fantasy_games': [
            {
                'name': "Zelda",
                'price': "{:,.2f}".format(140).replace('.', ','),
                'img': "games/images/1.jpeg"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg"
            },
            {
                'name': "Assassin's Creed",
                'price': "{:,.2f}".format(50).replace('.', ','),
                'img': "games/images/5.jpg"
            },
                        {
                'name': "Zelda",
                'price': "{:,.2f}".format(140).replace('.', ','),
                'img': "games/images/1.jpeg"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg"
            },
            {
                'name': "Assassin's Creed",
                'price': "{:,.2f}".format(50).replace('.', ','),
                'img': "games/images/5.jpg"
            },
                        {
                'name': "Zelda",
                'price': "{:,.2f}".format(140).replace('.', ','),
                'img': "games/images/1.jpeg"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg"
            },
            {
                'name': "Assassin's Creed",
                'price': "{:,.2f}".format(50).replace('.', ','),
                'img': "games/images/5.jpg"
            },
        ],

        'hero_games': [
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg"
            },
                        {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg"
            },
                        {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg"
            },
                        {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg"
            },
        ],
    }
    
    return render(request, "games/games_by_category.html", context)
