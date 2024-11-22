from django.contrib.auth import authenticate, login as auth_login
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .Books_Forms import BooksForm
from .models import *

# Create your views here.

def home(request):
    return render(request, template_name='bmHome/home.html')

def subscription(request):
    if request.method == 'POST':
        return redirect(reverse('sub_base'))
    return render(request, 'login_signup_subscription/subscription.html')

def books(request):
    return render(request, template_name='bmHome/books.html')

def contacts(request):
    return render(request, template_name='bmHome/contacts.html')

def litshelf(request):
    return render(request, template_name='bmHome/litshelf.html')

def academic(request):
    all_books = Book.objects.all()
    item = {
        'all_books': all_books,
    }
    return render(request, template_name='Buy_Books/academic.html', context=item)

def books_details(request, book_id):
    product = Book.objects.get(pk=book_id)
    context = {
        'product': product,
    }
    return render(request, template_name='Buy_Books/books_details.html', context=context)

def upload_Books(request):
    form = BooksForm()
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, template_name='Buy_Books/books_forms.html', context=context)

def update_product(request, book_id):
    books = Book.objects.get(pk=book_id)
    form = BooksForm(instance=books)
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES, instance=books)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, template_name='Buy_Books/books_details.html', context=context)

def fiction(request):
    all_books = Book.objects.all()
    item = {
        'all_books': all_books,
    }
    return render(request, template_name='Buy_Books/fiction.html', context=item)

def novel(request):
    return render(request, template_name='Buy_Books/novel.html')

def thriller(request):
    return render(request, template_name='Buy_Books/thriller.html')

def poetry(request):
    return render(request, template_name='Buy_Books/poetry.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        # authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Optional: Check user type if your user model has it
            if hasattr(user, 'userprofile') and user.userprofile.user_type == user_type:
                login(request, user)  # Only call login if user is authenticated
                return redirect('log_home')  # Redirect to the home page or another page after login
            else:
                messages.error(request, "Incorrect user type selected.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login_signup_subscription/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Create new user
        try:
            user = User.objects.create_user(
                username=username,  # Ensure email is set as username
                email=email
            )
            user.set_password(password)
            user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')  # Redirect to login page after successful signup
        except IntegrityError:
            messages.error(request, "An account with this email already exists.")
            return redirect('signup')

    return render(request, 'login_signup_subscription/signup.html')

def forget_pass(request):
    return render(request, template_name='login_signup_subscription/forget_pass.html')

def login_with(request):
    return render(request, template_name='login_signup_subscription/login_with.html')

def payment(request):
    return render(request, template_name='login_signup_subscription/payment.html')

def log_base(request):
    return render(request, template_name='login_user/log_base.html')

def log_navbar(request):
    return render(request, template_name='login_user/log_navbar.html')

def log_home(request):
    return render(request, template_name='login_user/log_home.html')

def log_help(request):
    return render(request, template_name='login_user/log_help.html')

def log_profile(request):
    return render(request, template_name='login_user/log_profile.html')

def u_help(request):
    return render(request, template_name='subscribed_user/u_help.html')

def sub_profile(request):
    return render(request, template_name='subscribed_user/sub_profile.html')

def sub_navbar(request):
    return render(request, template_name='subscribed_user/sub_navbar.html')

def sub_base(request):
    return render(request, template_name='subscribed_user/sub_base.html')

def r_academic(request):
    return render(request, template_name='rent_Books/r_academic.html')

def r_fiction(request):
    return render(request, template_name='Rent_Books/r_fiction.html')

def r_novel(request):
    return render(request, template_name='Rent_Books/r_novel.html')

def r_thriller(request):
    return render(request, template_name='Rent_Books/r_thriller.html')

def r_poetry(request):
    return render(request, template_name='Rent_Books/r_poetry.html')

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