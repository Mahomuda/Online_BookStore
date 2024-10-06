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
from myapp import views as myapp_views
from myapp import views as buy_books_views
from myapp import views as login_signin_subscription
from myapp import views as subscribed_user
from myapp import views as login_user
from myapp.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp_views.home, name='home'),
    path('books/',myapp_views.books, name='books'),
    path('contacts/',myapp_views.contacts, name='contacts'),

    path('academic/', buy_books_views.academic, name='academic'),
    path('fiction/', buy_books_views.fiction, name='fiction'),
    path('novel/', buy_books_views.novel, name='novel'),
    path('thriller/', buy_books_views.thriller, name='thriller'),
    path('poetry/', buy_books_views.poetry, name='poetry'),

    path('login/', login_signin_subscription.login, name='login'),
    path('signin/', login_signin_subscription.signin, name='signin'),
    path('subscription/', login_signin_subscription.subscription, name='subscription'),
    path('forget_pass/', login_signin_subscription.forget_pass, name='forget_pass'),
    path('login_with/', login_signin_subscription.login_with, name='login_with'),
    path('payment/', login_signin_subscription.payment, name='payment'),

    path('u_help/', subscribed_user.u_help, name='u_help'),
    path('sub_profile/', subscribed_user.sub_profile, name='profile'),
    path('rented_books/', subscribed_user.rented_books, name='rented_books'),
    path('sub_base/', subscribed_user.sub_base, name='sub_base'),
    path('sub_navbar/', subscribed_user.sub_navbar, name='sub_navbar'),

    path('log_help/', login_user.log_help, name='log_help'),
    path('log_profile/', login_user.log_profile, name='log_profile'),
    path('log_books/', login_user.log_books, name='log_books'),
    path('log_base/', login_user.log_base, name='log_base'),
    path('log_navbar/', login_user.log_navbar, name='log_navbar'),

]
