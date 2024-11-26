from django.db import models
from django.conf import settings
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    is_admin = models.BooleanField(verbose_name='Is Admin', default=False)
    is_user = models.BooleanField( verbose_name= 'Is user', default=False)
    is_shopowner = models.BooleanField( verbose_name= 'Is shopowner', default=False)
# Book model
class Book(models.Model):
    book_id = models.IntegerField()
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=200)
    rentable = models.CharField(max_length=200, blank=True, null=True)
    availability = models.CharField(max_length=200, blank=True, null=True)
    review = models.TextField(max_length=2000, blank=True, null=True)
    image = models.ImageField(upload_to='Books', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.book_name

# Author model
class Author(models.Model):
    author_name = models.CharField(max_length=200)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='Author', blank=True, null=True)

    def __str__(self):
        return self.author_name

# Shop model
class Shop(models.Model):
    shop_id = models.IntegerField(blank=True, null=True)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    shop_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    contact_number = models.IntegerField()

    def __str__(self):
        return self.shop_name

# Order model
class Order(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_orders'  # Unique related_name for Order
    )
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = (
        ('buy', 'Buy'),
        ('rent', 'Rent'),
    )
    status = models.CharField(max_length=200, choices=order_status, blank=True, null=True)

# Rider model
class Rider(models.Model):
    rider_id = models.IntegerField(blank=True, null=True)
    rider_name = models.CharField(max_length=200, blank=True, null=True)
    contact_number = models.IntegerField()

    def __str__(self):
        return self.rider_name

# Payment model
class Payment(models.Model):
    payment_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_payments'  # Unique related_name for Payment
    )
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=200)
    amount = models.IntegerField()
