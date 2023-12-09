# movies/admin.py
from django.contrib import admin
from .models import Movie
from .models import Category

admin.site.register(Movie)
admin.site.register(Category)
