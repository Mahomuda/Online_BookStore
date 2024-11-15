from django.forms import ModelForm
from .models import *


class BooksForm(ModelForm):
    class Meta:
       model = Book
       fields = '__all__'
