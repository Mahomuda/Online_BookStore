from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    book_id = models.IntegerField()
    book_name = models.CharField(max_length=200)
    price = models.IntegerField()
    genre = models.CharField(max_length=200)
    rentable = models.CharField(max_length=200, blank=True, null= True)
    availability = models.CharField(max_length=200,blank=True, null= True )
    review = models.TextField(max_length=2000, blank=True, null= True)

    def __str__(self):
        return f" name: self.book_name, gener: self.gener"

class Author (models.Model):
    author_name = models.CharField(max_length=200)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null= True)

    def __str__(self):
        return f" name: self.author_name, book: self.book_name"


class Order(models.Model):
    order_id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null= True)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null= True)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    order_date= models.DateTimeField(auto_now_add=True,auto_now=False)
    order_status = (
        ('buy', 'buy'),
        ('rent', 'rent'),
    )
    status=models.CharField(max_length=200, choices= order_status,blank=True, null= True)
    #riderid: int
    def __str__(self):
        return f" name: self.user_id, book: self.book_name, "

class Shop(models.Model):
    shop_id = models.IntegerField(blank=True, null= True)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null= True)
    shop_name = models.CharField(max_length=200,blank=True, null=True)
    address= models.CharField(max_length=200, blank=True, null=True)
    contact_number=models.IntegerField()
    def __str__(self):
        return f" name: self.shop_name, address: self.address, "
