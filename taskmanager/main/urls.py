
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index),
    path('index_2', views.index_2),
    path('index_3', views.index_3),
    path('index_4', views.index_4),
    path('error', views.error),
    path('about', views.about),
    path('blog', views.blog),
    path('cart', views.cart),
    path('checkout', views.checkout),
    path('compare', views.compare),
    path('contact', views.contact),
    path('forgot-password', views.forgot_password),
    path('login', views.login),
    path('product', views.product),
    path('register', views.register),
    path('shop', views.shop),
    path('single-blog', views.single_blog),
    path('terms-conditions', views.terms_conditions),
    path('wishlist', views.wishlist),
]
