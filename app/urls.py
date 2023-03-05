from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home),
    path('home', views.home, name="home"),
    path('seller', views.seller),
    path('shop', views.shop),
    path('wishlist', views.wishlist),
    path('cart', views.cart),
    path('categories', views.categories),

    path("login", views.loginpage, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("register", views.registerpage, name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
