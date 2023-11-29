from django.shortcuts import render


def home(request):
    context = {
        'movies': [
            {
                'name': "Titanic",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/1.jpg",
                'slug': "titanic"
            },
            {
                'name': "MIB",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/2.jpg",
                'slug': "mib"
            },
            {
                'name': "Interstellar",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/3.png",
                'slug': "interstellar"
            },
            {
                'name': "Avengers: Endgame",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "movies/images/4.jpg",
                'slug': "avengers-endgame"
            },
            {
                'name': "Liga da Justiça",
                'price': "{:,.2f}".format(22).replace('.', ','),
                'img': "movies/images/5.jpg",
                'slug': "liga-da-justica"
            },
            {
                'name': "Harry Potter",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/6.jpg",
                'slug': "harry-potter"
            },
            {
                'name': "Titanic",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/1.jpg",
                'slug': "titanic"
            },
            {
                'name': "MIB",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/2.jpg",
                'slug': "mib"
            },
            {
                'name': "Interstellar",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/3.png",
                'slug': "interstellar"
            },
            {
                'name': "Avengers: Endgame",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "movies/images/4.jpg",
                'slug': "avengers-endgame"
            }
        ],
        'games': [
            {
                'name': "Zelda",
                'price': "{:,.2f}".format(140).replace('.', ','),
                'img': "games/images/1.jpeg",
                'slug': "zelda"
            },
            {
                'name': "Doom",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/2.jpg",
                'slug': "doom"
            },
            {
                'name': "Watch Dogs",
                'price': "{:,.2f}".format(40).replace('.', ','),
                'img': "games/images/3.jpg",
                'slug': "watch-dogs"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg",
                'slug': "spider-man"
            },
            {
                'name': "Assassin's Creed",
                'price': "{:,.2f}".format(50).replace('.', ','),
                'img': "games/images/5.jpg",
                'slug': "assassins-creed"
            },
            {
                'name': "Red Alert 3",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/6.jpg",
                'slug': "red-alert-3"
            },
            {
                'name': "Zelda",
                'price': "{:,.2f}".format(140).replace('.', ','),
                'img': "games/images/1.jpeg",
                'slug': "zelda"
            },
            {
                'name': "Doom",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/2.jpg",
                'slug': "doom"
            },
            {
                'name': "Watch Dogs",
                'price': "{:,.2f}".format(40).replace('.', ','),
                'img': "games/images/3.jpg",
                'slug': "watch-dogs"
            },
            {
                'name': "Spider-man",
                'price': "{:,.2f}".format(120).replace('.', ','),
                'img': "games/images/4.jpg",
                'slug': "spider-man"
            },
            {
                'name': "Assassin's Creed",
                'price': "{:,.2f}".format(50).replace('.', ','),
                'img': "games/images/5.jpg",
                'slug': "assassins-creed"
            },
            {
                'name': "Red Alert 3",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "games/images/6.jpg",
                'slug': "red-alert-3"
            }
        ],
        'musics': [
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg",
                'slug': "kid-abelha"
            },
            {
                'name': "The Beatles",
                'price': "{:,.2f}".format(5).replace('.', ','),
                'img': "musics/images/2.jpg",
                'slug': "the-beatles"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg",
                'slug': "iron-maiden"
            },
            {
                'name': "Linkin Park",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "musics/images/4.jpg",
                'slug': "linkin-park"
            },
            {
                'name': "Michael Jackson",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "musics/images/5.jpg",
                'slug': "michael-jackson"
            },
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg",
                'slug': "kid-abelha"
            },
            {
                'name': "The Beatles",
                'price': "{:,.2f}".format(5).replace('.', ','),
                'img': "musics/images/2.jpg",
                'slug': "the-beatles"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg",
                'slug': "iron-maiden"
            },
            {
                'name': "Linkin Park",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "musics/images/4.jpg",
                'slug': "linkin-park"
            },
            {
                'name': "Michael Jackson",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "musics/images/5.jpg",
                'slug': "michael-jackson"
            }
        ]
    }
    return render(request, "home/home.html", context)
