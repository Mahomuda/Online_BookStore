import uuid

from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('normal', 'User'),
        ('shopowner', 'Shop Owner'),
    )
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)  # Ensure username is unique
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='normal')
    address = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='user_groups',  # Unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_permissions',  # Unique related_name
        blank=True
    )

    def __str__(self):
        return self.username


class Sub_user(AbstractUser):
    sub_user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    linked_user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name='sub_users'
    )  # Renamed from 'username' to avoid conflict
    address = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='sub_user_groups',  # Unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='sub_user_permissions',  # Unique related_name
        blank=True
    )

    def __str__(self):
        return f"Sub User: {self.linked_user}" if self.linked_user else "Unlinked Sub User"

# Book model
class Book(models.Model):
    book_id = models.IntegerField()
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=200)

    stock_quantity = models.IntegerField(default=0) 
    rentable = models.CharField(max_length=200, blank=True, null= True)
    availability = models.CharField(max_length=200,blank=True, null= True )
    review = models.TextField(max_length=2000, blank=True, null= True)
    image = models.ImageField(upload_to= 'Books/', blank=True, null=True)
    description = models.TextField(blank=True, null= True)

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
    status = models.CharField(max_length=200, choices = order_status, blank=True, null=True)

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


    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    # Add other fields as necessary

    def __str__(self):
        return f"{self.user.username}'s profile"
    

class SubProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=100)
    subscription_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()

    def __str__(self):
        return f"Subscription Profile for {self.user.username}"
