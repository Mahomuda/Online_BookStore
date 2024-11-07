"""
URL configuration for bmSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static

from myapp import views as myapp_views
from myapp import views as buy_books_views
from myapp import views as login_signup_subscription
from myapp import views as login_user
from myapp import views as subscribed_user
from myapp import views as rent_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',myapp_views.home, name='home'),
    path('contacts/',myapp_views.contacts, name='contacts'),
    path('books/',myapp_views.books, name='books'),
    path('',myapp_views.litshelf, name='litshelf'),


    path('academic/', buy_books_views.academic, name='academic'),
    path('fiction/', buy_books_views.fiction, name='fiction'),
    path('novel/', buy_books_views.novel, name='novel'),
    path('thriller/', buy_books_views.thriller, name='thriller'),
    path('poetry/', buy_books_views.poetry, name='poetry'),

    path('login/', login_signup_subscription.login, name='login'),
    path('signup/', login_signup_subscription.signup, name='signup'),
    path('subscription/', login_signup_subscription.subscription, name='subscription'),
    path('forget_pass/', login_signup_subscription.forget_pass, name='forget_pass'),
    path('login_with/', login_signup_subscription.login_with, name='login_with'),
    path('payment/', login_signup_subscription.payment, name='payment'),

    path('log_base/', login_user.log_base, name='log_base'),
    path('log_navbar/', login_user.log_navbar, name='log_navbar'),
    path('log_help/', login_user.log_help, name='log_help'),
    path('log_profile/', login_user.log_profile, name='log_profile'),

    path('u_help/', subscribed_user.u_help, name='sub_help'),
    path('sub_profile/', subscribed_user.sub_profile, name='sub_profile'),
    path('subscribed_user/sub_base/', subscribed_user.sub_base, name='sub_base'),
    path('sub_navbar/', subscribed_user.sub_navbar, name='sub_navbar'),

    path('r_academic/', rent_books.r_academic, name='r_academic'),
    path('r_fiction/', rent_books.r_fiction, name='r_fiction'),
    path('r_novel/', rent_books.r_novel, name='r_novel'),
    path('r_thriller/', rent_books.r_thriller, name='r_thriller'),
    path('r_poetry/', rent_books.r_poetry, name='r_poetry'),



]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



