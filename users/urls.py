from django.urls import path

from . import users_views

urlpatterns = [
    path("profile/", users_views.my_profile, name= "my_profile"),
    path("login/", users_views.login, name= "login"),
    path("cart/", users_views.cart, name= "cart")
]
