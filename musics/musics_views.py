from django.shortcuts import render, get_object_or_404
from .models import Category, Music

def musics_by_category(request):
    context = {
        'musics_by_categories': Category.objects.filter(music__isnull=False).distinct()
    }
    return render(request, "musics/musics_by_category.html", context)


def music_details(request, slug):    
    music = get_object_or_404(Music, slug=slug)
    
    context = {
        'music': music
    }

    return render(request, "musics/music_details.html", context)
