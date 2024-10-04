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

]
