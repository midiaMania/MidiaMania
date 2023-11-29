from django.urls import path

from . import games_views

urlpatterns = [
    path("", games_views.games_by_category, name="games_by_category"),
    path("<slug:slug>", games_views.game_details, name="game_details")
]
