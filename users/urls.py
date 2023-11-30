from django.urls import path

from . import users_views

urlpatterns = [
    path("", users_views.my_profile, name= "my_profile")
]
