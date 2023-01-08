from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def index_2(request):
    return render(request, 'main/index_2.html')


def index_3(request):
    return render(request, 'main/index_3.html')


def index_4(request):
    return render(request, 'main/index_4.html')


def error(request):
    return render(request, 'main/error.html')


def about(request):
    return render(request, 'main/about.html')


def blog(request):
    return render(request, 'main/blog.html')


def cart(request):
    return render(request, 'main/cart.html')


def checkout(request):
    return render(request, 'main/checkout.html')


def compare(request):
    return render(request, 'main/compare.html')


def contact(request):
    return render(request, 'main/contact.html')


def forgot_password(request):
    return render(request, 'main/forgot_password.html')


def login(request):
    return render(request, 'main/login.html')


def product(request):
    return render(request, 'main/product.html')


def register(request):
    return render(request, 'main/register.html')


def shop(request):
    return render(request, 'main/shop.html')


def single_blog(request):
    return render(request, 'main/single_blog.html')


def terms_conditions(request):
    return render(request, 'main/terms_conditions.html')


def wishlist(request):
    return render(request, 'main/wishlist.html')
