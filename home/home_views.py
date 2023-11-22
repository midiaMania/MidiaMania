from django.shortcuts import render

def home(request):
    context = {
        'movies': [
            {
                'name': "Titanic",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/1.jpg"
            },
            {
                'name': "MIB",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/2.jpg"
            },
            {
                'name': "Interstellar",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/3.png"
            },
            {
                'name': "Avengers: Endgame",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "movies/images/4.jpg"
            },
            {
                'name': "Liga da Justiça",
                'price': "{:,.2f}".format(22).replace('.', ','),
                'img': "movies/images/5.jpg"
            },
            {
                'name': "Harry Potter",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/6.jpg"
            },
            {
                'name': "Titanic",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/1.jpg"
            },
            {
                'name': "MIB",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/2.jpg"
            },
            {
                'name': "Interstellar",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/3.png"
            },
            {
                'name': "Avengers: Endgame",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "movies/images/4.jpg"
            }
        ],
        'games': [
            {
                'name': "Zelda",
                'price': "{:,.2f}".format(140).replace('.', ','),
                'img': "games/images/1.jpeg"
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
                'name': "Red Alert 3",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/6.jpg"
            },
            {
                'name': "Zelda",
                'price': "{:,.2f}".format(140).replace('.', ','),
                'img': "games/images/1.jpeg"
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
                'name': "Red Alert 3",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/6.jpg"
            }
        ],
        'musics': [
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg"
            },
            {
                'name': "The Beatles",
                'price': "{:,.2f}".format(5).replace('.', ','),
                'img': "musics/images/2.jpg"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg"
            },
            {
                'name': "Linkin Park",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "musics/images/4.jpg"
            },
            {
                'name': "Michael Jackson",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "musics/images/5.jpg"
            },
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg"
            },
            {
                'name': "The Beatles",
                'price': "{:,.2f}".format(5).replace('.', ','),
                'img': "musics/images/2.jpg"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg"
            },
            {
                'name': "Linkin Park",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "musics/images/4.jpg"
            },
            {
                'name': "Michael Jackson",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "musics/images/5.jpg"
            }
        ]
    }
    return render(request, "home/home.html", context)
