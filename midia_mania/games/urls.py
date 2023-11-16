from django.urls import path

from . import games_views

urlpatterns = [
    path("", games_views.games_by_category, name="games_by_category"),
]