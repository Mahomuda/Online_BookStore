from django.contrib import admin
from .models import Book, Author, Order

# Register your models here.
admin.site.register([Book, Author, Order])