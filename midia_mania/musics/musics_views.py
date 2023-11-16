from django.shortcuts import render

def musics_by_category(request):
    return render(request, "musics/musics_by_category.html")
