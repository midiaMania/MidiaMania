from django.urls import path

from . import movies_views

urlpatterns = [
    path("", movies_views.movies_by_category, name="movies_by_category"),
]