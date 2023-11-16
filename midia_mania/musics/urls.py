from django.urls import path

from . import musics_views

urlpatterns = [
    path("", musics_views.musics_by_category, name="musics_by_category"),
]