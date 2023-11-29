from django.shortcuts import render


def musics_by_category(request):
    context = {
        'pop_musics': [
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg",
                'slug': "pop"
            },
            {
                'name': "Michael Jackson",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "musics/images/5.jpg",
                'slug': "pop"
            },
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg",
                'slug': "pop"
            },
            {
                'name': "Michael Jackson",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "musics/images/5.jpg",
                'slug': "pop"
            },
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg",
                'slug': "pop"
            },
            {
                'name': "Michael Jackson",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "musics/images/5.jpg",
                'slug': "pop"
            },
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg",
                'slug': "pop"
            },
            {
                'name': "Michael Jackson",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "musics/images/5.jpg",
                'slug': "pop"
            },
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg",
                'slug': "pop"
            },
            {
                'name': "Michael Jackson",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "musics/images/5.jpg",
                'slug': "pop"
            },
        ],

        'rock_musics': [
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg",
                'slug': "rock"
            },
            {
                'name': "The Beatles",
                'price': "{:,.2f}".format(5).replace('.', ','),
                'img': "musics/images/2.jpg",
                'slug': "rock"
            },
            {
                'name': "Linkin Park",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "musics/images/4.jpg",
                'slug': "rock"
            },
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg",
                'slug': "rock"
            },
            {
                'name': "The Beatles",
                'price': "{:,.2f}".format(5).replace('.', ','),
                'img': "musics/images/2.jpg",
                'slug': "rock"
            },
            {
                'name': "Linkin Park",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "musics/images/4.jpg",
                'slug': "rock"
            },
            {
                'name': "Kid Abelha",
                'price': "{:,.2f}".format(4).replace('.', ','),
                'img': "musics/images/1.jpg",
                'slug': "rock"
            },
            {
                'name': "The Beatles",
                'price': "{:,.2f}".format(5).replace('.', ','),
                'img': "musics/images/2.jpg",
                'slug': "rock"
            },
            {
                'name': "Linkin Park",
                'price': "{:,.2f}".format(10).replace('.', ','),
                'img': "musics/images/4.jpg",
                'slug': "rock"
            },
        ],

        'metal_musics': [
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg",
                'slug': "metal"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg",
                'slug': "metal"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg",
                'slug': "metal"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg",
                'slug': "metal"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg",
                'slug': "metal"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg",
                'slug': "metal"
            },
            {
                'name': "Iron Maiden",
                'price': "{:,.2f}".format(7).replace('.', ','),
                'img': "musics/images/3.jpg",
                'slug': "metal"
            },
        ],
    }
    return render(request, "musics/musics_by_category.html", context)


def music_details(request, slug):
    context = {
        'slug': slug,
        'title': 'Música! O melhor da música do Kid Abelha',
        'img': 'musics/images/1.jpg',
        'artist': 'Kid Abelha',
        'record_label': 'WARNER MUSIC',
        'release_date': 2001,
        'price': "{:,.2f}".format(14).replace('.', ','),
        'num_tracks': 14,
        'format': 'CD, DVD e Vinil',
        'tracks': [
            "Como Eu Quero",
            "Alice (Não Me Escreva Aquela Carta De Amor)",
            "Porque Não Eu?",
            "Amanhã É 23",
            "Pintura Íntima",
            "Grand Hotel",
            "Dizer Não É Dizer Sim",
            "Todo O Meu Ouro",
            "Educação Sentimental II",
            "Lágrimas E Chuva",
            "Nada Tanto Assim",
            "Seu Espião",
            "Solidão Que Nada",
            "A Fórmula Do Amor"
        ],
        'categories': ['POP', 'Rock', 'Alternativo']
    }

    return render(request, "musics/music_details.html", context)
