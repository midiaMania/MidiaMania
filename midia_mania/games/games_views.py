from django.shortcuts import render

def games_by_category(request):
    return render(request, "games/games_by_category.html")
