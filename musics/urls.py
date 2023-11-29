from django.urls import path

from . import musics_views

urlpatterns = [
    path("", musics_views.musics_by_category, name="musics_by_category"),
    path("<slug:slug>", musics_views.music_details, name="music_details")
]
