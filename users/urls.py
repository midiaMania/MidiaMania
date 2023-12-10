from django.urls import path

from . import users_views
from .users_views import My_profile, Login, Logout, SignUp

urlpatterns = [
    path("profile/", My_profile.as_view(), name="my_profile"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("checkout/", users_views.checkout, name="checkout"),
    path("cart/", users_views.cart, name="cart"),
    path("movies/<slug:slug>/add_to_cart/",users_views.add_movie_to_cart, name="add_movie_to_cart"),
    path("musics/<slug:slug>/add_to_cart/",users_views.add_music_to_cart, name="add_music_to_cart"),
    path("games/<slug:slug>/add_to_cart/",users_views.add_game_to_cart, name="add_game_to_cart"),
]
