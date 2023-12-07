from django.urls import path

from . import users_views
from .users_views import My_profile

urlpatterns = [
    path("profile/", My_profile.as_view(), name="my_profile"),
    path("login/", users_views.login, name="login"),
    path("signup/", users_views.signup, name="signup"),
    path("checkout/", users_views.checkout, name="checkout"),
    path("cart/", users_views.cart, name="cart")
]
