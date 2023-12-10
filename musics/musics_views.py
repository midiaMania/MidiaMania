from django.shortcuts import render, get_object_or_404
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
    music = get_object_or_404(Music, slug=slug)
    
    context = {
        'music': music
    }

    return render(request, "musics/music_details.html", context)
