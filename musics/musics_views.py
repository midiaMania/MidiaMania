from django.shortcuts import render
from .models import Category, Music

def musics_by_category(request):
    categories = Category.objects.all()
    musics_by_category = {}
    for category in categories:
        musics = category.music_set.all()
        musics_list = []
        for music in musics:
            musics_list.append({
                'name': music.name,
                'price': "{:,.2f}".format(music.price).replace('.', ','),
                'img': music.image.url,
                'slug': music.slug
        })
        musics_by_category[category.name] = musics_list

    context = {
        'musics_by_category': musics_by_category
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
