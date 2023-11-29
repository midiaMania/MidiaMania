from django.shortcuts import render


def movies_by_category(request):
    context = {
        'action_movies': [
            {
                'name': "MIB",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/2.jpg",
                'slug': "action"
            },
            {
                'name': "Avengers: Endgame",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "movies/images/4.jpg",
                'slug': "action"
            },
            {
                'name': "Liga da Justiça",
                'price': "{:,.2f}".format(22).replace('.', ','),
                'img': "movies/images/5.jpg",
                'slug': "action"
            },
            {
                'name': "Harry Potter",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/6.jpg",
                'slug': "action"
            },
            {
                'name': "MIB",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/2.jpg",
                'slug': "action"
            },
            {
                'name': "Avengers: Endgame",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "movies/images/4.jpg",
                'slug': "action"
            },
            {
                'name': "Liga da Justiça",
                'price': "{:,.2f}".format(22).replace('.', ','),
                'img': "movies/images/5.jpg",
                'slug': "action"
            },
            {
                'name': "Harry Potter",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/6.jpg",
                'slug': "action"
            },
            {
                'name': "MIB",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/2.jpg",
                'slug': "action"
            },
            {
                'name': "Avengers: Endgame",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "movies/images/4.jpg",
                'slug': "action"
            },
            {
                'name': "Liga da Justiça",
                'price': "{:,.2f}".format(22).replace('.', ','),
                'img': "movies/images/5.jpg",
                'slug': "action"
            },
            {
                'name': "Harry Potter",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/6.jpg",
                'slug': "action"
            }
        ],

        'drama_movies': [
            {
                'name': "Titanic",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/1.jpg",
                'slug': "drama"
            },
            {
                'name': "Interstellar",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/3.png",
                'slug': "drama"
            },
            {
                'name': "Harry Potter",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/6.jpg",
                'slug': "drama"
            },
            {
                'name': "Titanic",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/1.jpg",
                'slug': "drama"
            },
            {
                'name': "Interstellar",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/3.png",
                'slug': "drama"
            },
            {
                'name': "Harry Potter",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/6.jpg",
                'slug': "drama"
            },
            {
                'name': "Titanic",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/1.jpg",
                'slug': "drama"
            },
            {
                'name': "Interstellar",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/3.png",
                'slug': "drama"
            },
            {
                'name': "Harry Potter",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/6.jpg",
                'slug': "drama"
            }
        ],

        'hero_movies': [
            {
                'name': "Avengers: Endgame",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "movies/images/4.jpg",
                'slug': "hero"
            },
            {
                'name': "Liga da Justiça",
                'price': "{:,.2f}".format(22).replace('.', ','),
                'img': "movies/images/5.jpg",
                'slug': "hero"
            },
            {
                'name': "Avengers: Endgame",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "movies/images/4.jpg",
                'slug': "hero"
            },
            {
                'name': "Liga da Justiça",
                'price': "{:,.2f}".format(22).replace('.', ','),
                'img': "movies/images/5.jpg",
                'slug': "hero"
            },
            {
                'name': "Avengers: Endgame",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "movies/images/4.jpg",
                'slug': "hero"
            },
            {
                'name': "Liga da Justiça",
                'price': "{:,.2f}".format(22).replace('.', ','),
                'img': "movies/images/5.jpg",
                'slug': "hero"
            }
        ]
    }

    return render(request, "movies/movies_by_category.html", context)


def movie_details(request, slug):
    context = {
        'slug': slug,
        'title': 'Avengers: Endgame',
        'img': 'movies/images/4.jpg',
        'directors': 'Anthony Russo e Joe Russo',
        'rating': 12,
        'synopsis': 'Após os eventos devastadores de "Vingadores: Guerra Infinita", o universo está em ruínas devido aos esforços do Titã Louco, Thanos. Com a ajuda de aliados remanescentes, os Vingadores devem se reunir mais uma vez a fim de desfazer as ações de Thanos e restaurar a ordem no universo de uma vez por todas, não importando as consequências.',
        'release_date': 2019,
        'running_time': 181,
        'price': "{:,.2f}".format(14).replace('.', ','),
        'categories': ['Ação', 'Aventura', 'Fantasia']
    }

    return render(request, "movies/movie_details.html", context)
