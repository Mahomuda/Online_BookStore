from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .Books_Forms import BooksForm
from .form import SignupForm, loginForm
from .models import *
from django.contrib.auth import authenticate,login

# Create your views here.

def home(request):
    return render(request, template_name='bmHome/home.html')

def subscription(request):
    if request.method == 'POST':
        return redirect(reverse('sub_base'))
    return render(request, 'login_signup_subscription/subscription.html')

def books(request):
    genre_filter = request.GET.get('genre', None)
    if genre_filter:
        all_books = Book.objects.filter(genre__iexact=genre_filter)
    else:
        all_books = Book.objects.all()

    item = {
        'all_books': all_books,
        'genre': genre_filter,
    }
    return render(request, template_name='bmHome/books.html', context=item)

def books_details(request, book_id):
    allbooks = Book.objects.get(pk=book_id)
    context = {
        'allbooks': allbooks,
    }
    return render(request, template_name='bmHome/books_details.html', context=context)


def contacts(request):
    return render(request, template_name='bmHome/contacts.html')

def litshelf(request):
    return render(request, template_name='bmHome/litshelf.html')

def signup(request):
   msg = None
   if request.method == 'POST':
       form = SignupForm(request.POST)
       if form.is_valid():
           user= form.save()
           msg = 'user created'
           return redirect('login')
       else:
           msg = 'Username already exists or Password is not valid (Password will have 8 characters and it will be unique)'
   else:
       form = SignupForm()
   context = {
       'form':form,
       'msg': msg
   }
   return render(request, template_name='login_signup_subscription/signup.html',context=context)


def login(request):
   form = loginForm(request.POST or None)
   msg = None
   if request.method == "POST" and form.is_valid():
       username = form.cleaned_data.get('username')
       password = form.cleaned_data.get('password')
       user = authenticate(username = username, password = password)
       if user is not None and user.is_shopowner:
           return redirect('shop_profile')
       elif user is not None and user.is_user:
           return redirect('log_profile')
       else:
           msg = 'invalid credentials'
   else:
       msg = 'error validating form'
   context = {
       'form' : form,
       'msg' : msg
   }
   return render(request, template_name='login_signup_subscription/login.html', context=context)

def forget_pass(request):
    return render(request, template_name='login_signup_subscription/forget_pass.html')

def payment(request):
    return render(request, template_name='login_signup_subscription/payment.html')

def process_payment(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        transaction_id = request.POST.get('transaction_id')
        amount = request.POST.get('amount')

        # Placeholder logic for payment validation
        if phone and transaction_id and amount:
            # Log or process payment
            messages.success(request, "Payment processed successfully!")
            return redirect('payment')  # Redirect back to the payment page or another relevant page
        else:
            messages.error(request, "Invalid payment details. Please try again.")
            return redirect('payment')

    return redirect('payment')



def log_base(request):
    return render(request, template_name='login_user/log_base.html')

def log_navbar(request):
    return render(request, template_name='login_user/log_navbar.html')

def log_book(request):
    genre_filter = request.GET.get('genre', None)
    if genre_filter:
        all_books = Book.objects.filter(genre__iexact=genre_filter)
    else:
        all_books = Book.objects.all()

    item = {
        'all_books': all_books,
        'genre': genre_filter,
    }
    return render(request, template_name='login_user/log_book.html', context=item)
def log_books_details(request, book_id):
    allbooks = Book.objects.get(pk=book_id)
    context = {
        'allbooks': allbooks,
    }
    return render(request, template_name='login_user/log_books_details.html', context=context)
def log_help(request):
    return render(request, template_name='login_user/log_help.html')

def log_profile(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')  # Redirect to login page if not logged in

    userdetails = request.user  # Should get the details of the logged-in user
    context = {
        'userdetails': userdetails,
    }

    return render(request, 'login_user/log_profile.html', context)

def sub_help(request):
    return render(request, template_name='subscribed_user/sub_help.html')
def sub_profile(request):
    return render(request, template_name='subscribed_user/sub_profile.html')
def sub_navbar(request):
    return render(request, template_name='subscribed_user/sub_navbar.html')
def sub_base(request):
    return render(request, template_name='subscribed_user/sub_base.html')
def sub_books(request):
    allbooks = Book.objects.all()
    item = {
        'allbooks': allbooks,
    }
    return render(request, template_name='subscribed_user/sub_books.html',context=item)

def sub_rent_books(request):
    allbooks = Book.objects.filter(rentable= 'yes')
    item = {
        'allbooks': allbooks,
    }
    return render(request, 'subscribed_user/sub_rent_books.html', context= item)

def sub_books_details(request,book_id):
    allbooks = Book.objects.get(pk=book_id)
    item = {
        'allbooks': allbooks,
    }
    return render(request, template_name='subscribed_user/sub_books_details.html',context= item)

def shop_base(request):
    return render(request, template_name='shop_owner/shop_base.html')

def shop_navbar(request):
    return render(request, template_name='shop_owner/shop_navbar.html')

def shop_books(request):
    genre_filter = request.GET.get('genre', None)
    if genre_filter:
        all_books = Book.objects.filter(genre__iexact=genre_filter)
    else:
        all_books = Book.objects.all()

    item = {
        'all_books': all_books,
        'genre': genre_filter,
    }
    return render(request, template_name='shop_owner/shop_books.html', context=item)



def shop_help(request):
    return render(request, template_name='shop_owner/shop_help.html')

def shop_profile(request):
    return render(request, template_name='shop_owner/shop_profile.html')

def shop_payment(request):
    return render(request, template_name='shop_owner/shop_payment.html')

def shop_book_details(request,book_id):
    allbooks = Book.objects.get(pk = book_id)
    item = {
        'allbooks':allbooks,
    }
    return render(request,template_name = 'shop_owner/shop_book_details.html',context = item)

def upload_books(request):
    form = BooksForm()
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, template_name='shop_owner/books_form.html', context=context)

def update_books(request, book_id):
    allbooks = Book.objects.get(pk=book_id)
    form = BooksForm (instance=allbooks)
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES, instance=books)
        if form.is_valid():
            form.save()
            return redirect('shop_books')
    context = {'form': form}
    return render(request, template_name='shop_owner/books_form.html',context=context)

def delete_books(request,book_id):
   allbooks = Book.objects.get(pk=book_id)
   if request.method == 'POST':
       allbooks.delete()
       return redirect('home')
   return render(request, template_name = 'shop_owner\delete_books.html')

