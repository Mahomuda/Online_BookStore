from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .Books_Forms import BooksForm
from .form import SignupForm, ProfileUpdateForm, LoginForm, Sub_LoginForm
from .models import *
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Order
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404

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
        allbooks = Book.objects.filter(genre__iexact=genre_filter)
    else:
        allbooks = Book.objects.all()

    item = {
        'allbooks': allbooks,
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

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Pass the request and the user object to the login() function
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'login_signup_subscription/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)

                if user.user_type == 'normal':
                    return redirect('log_profile')
                elif user.user_type == 'shopowner':
                    return redirect('shop_profile')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'login_signup_subscription/login.html', {'form': form})


def subscription(request):
    if request.method == 'POST':
        form = Sub_LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = authenticate(request, username=username, password=password)

            if user is None:
                user = authenticate(request, username=email, password=password)

            if user is not None:

                return redirect('sub_profile')
            else:
                form.add_error(None, 'Invalid login credentials')
    else:
        form = Sub_LoginForm()
    return render(request, 'login_signup_subscription/subscription.html', {'form': form})


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
        allbooks = Book.objects.filter(genre__iexact=genre_filter)
    else:
        allbooks = Book.objects.all()

    item = {
        'all_books': allbooks,
        'genre': genre_filter,
    }
    return render(request, template_name='login_user/log_book.html', context=item)
def log_books_details(request, book_id):
    allbooks = Book.objects.get(id=book_id)
    context = {
        'allbooks': allbooks,
    }
    return render(request, template_name='login_user/log_books_details.html', context=context)



@login_required
def purchase_book(request, book_id):
    user = request.user 
    
    if hasattr(user, 'profile'):
        user_profile = user.profile
    else:
        user_profile = None  
  
    book = get_object_or_404(Book, pk=book_id)

    if book.stock_quantity > 0:

        order = Order.objects.create(
            user_id=request.user,
            book_name=book,
            amount=book.price,
            status='buy',
            phone=request.user.profile.phone
        )


        book.stock_quantity -= 1
        book.save()

        return render(request, 'purchase_success.html', {'order': order})
    else:
        return render(request, 'purchase_failed.html', {'message': 'Out of stock'})
    


def confirm_payment(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'login_user/confirm_payment.html', {'book': book})  # No need to include 'template/' in the path


def process_payment_for_book(request, book_id): 
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        phone = request.POST.get('phone')
        transaction_id = request.POST.get('transaction_id')
        amount = request.POST.get('amount')
       
        if phone and transaction_id and amount:

            book.is_sold = True
            book.save()
            messages.success(request, f"Payment successful for {book.book_name}. Transaction ID: {transaction_id}.")
            return redirect('payment_confirmation', book_id=book.id)  # Redirect to the confirmation page
        else:
            messages.error(request, "Please provide all the required details.")
            return redirect('process_payment', book_id=book.id)

    return render(request, 'login_user/process_payment_for_book.html', {'book': book})

def payment_confirmation(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'login_user/payment_confirmation.html', {'book': book})

def log_help(request):
    return render(request, template_name='login_user/log_help.html')


@login_required
def log_profile(request):
    return render(request, 'login_user/log_profile.html', {'user': request.user})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('log_profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'login_user/profile_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def sub_help(request):
    return render(request, template_name='subscribed_user/sub_help.html')

@login_required
def sub_profile(request):
    return render(request, template_name='subscribed_user/sub_profile.html',context={'user': request.user})

def update_sub_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('log_profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'subscribed_user/sub_profile_form.html', {'form': form})

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
def sub_rent_books_details(request,book_id):
    allbooks = Book.objects.get(pk=book_id)
    item = {
        'allbooks': allbooks,
    }
    return render(request, template_name='subscribed_user/sub_rent_books_details.html',context= item)


def rent_info(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        email = request.POST.get('email')
        address = request.POST.get('address')
        duration = request.POST.get('duration')
    return render(request, 'subscribed_user/rent_info.html', {'book': book})


def rent_confirmation(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'subscribed_user/rent_confirmation.html', {'book': book})


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

@login_required
def shop_profile(request):
    return render(request, 'shop_owner/shop_profile.html', {'user': request.user})

def shop_update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('log_profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'shop_owner/shop_profile_form.html', {'form': form})

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
   return redirect('payment') 


def view_sub_profile(request, user_id):
    sub_profile = get_object_or_404(SubProfile, user_id=user_id)
    return render(request, 'sub_profile.html', {'sub_profile': sub_profile})


