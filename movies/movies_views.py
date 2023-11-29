from django.shortcuts import render

def movies_by_category(request):
    context = {
        'action_movies': [
            {
                'name': "MIB",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/2.jpg"
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
                'name': "MIB",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/2.jpg"
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
                'name': "MIB",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/2.jpg"
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
            }
        ],

        'drama_movies': [
            {
                'name': "Titanic",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/1.jpg"
            },
            {
                'name': "Interstellar",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/3.png"
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
                'name': "Interstellar",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/3.png"
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
                'name': "Interstellar",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "movies/images/3.png"
            },
            {
                'name': "Harry Potter",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/6.jpg"
            }
        ],

        'hero_movies': [
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
                'name': "Avengers: Endgame",
                'price': "{:,.2f}".format(20).replace('.', ','),
                'img': "movies/images/4.jpg"
            },
            {
                'name': "Liga da Justiça",
                'price': "{:,.2f}".format(22).replace('.', ','),
                'img': "movies/images/5.jpg"
            }
        ]
    }
    
    return render(request, "movies/movies_by_category.html", context)


def movie_details(request, slug):
    context = {
        'slug': slug,
        'title': 'Avengers: Endgame',
        'img': 'movies/images/4.jpg',
        'release_date': 2019,
        'running_time': 181,
        'value': 4500,
        'categories': ['Ação', 'Aventura', 'Fantasia']    
    }
    
    return render(request, "movies/movie_details.html", context)
