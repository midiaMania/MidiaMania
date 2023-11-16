from django.shortcuts import render

def movies_by_category(request):
    return render(request, "movies/movies_by_category.html")
