from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, template_name='bmHome/home.html')

def books(request):
    return render(request, template_name='bmHome/books.html')

def contacts(request):
    return render(request, template_name='bmHome/contacts.html')



def academic(request):
    return render(request, template_name='Buy_Books/academic.html')
def fiction(request):
    return render(request, template_name='Buy_Books/fiction.html')
def novel(request):
    return render(request, template_name='Buy_Books/novel.html')
def thriller(request):
    return render(request, template_name='Buy_Books/thriller.html')
def poetry(request):
    return render(request, template_name='Buy_Books/poetry.html')


def login(request):
    return render(request, template_name='login_signin_subscription/login.html')
def signin(request):
    return render(request, template_name='login_signin_subscription/signin.html')
def subscription(request):
    return render(request, template_name='login_signin_subscription/subscription.html')
def forget_pass(request):
    return render(request, template_name='login_signin_subscription/forget_pass.html')
def login_with(request):
    return render(request, template_name='login_signin_subscription/login_with.html')
def payment(request):
    return render(request, template_name='login_signin_subscription/payment.html')


def u_help(request):
    return render(request, template_name='subscribed_user/u_help.html')
def sub_profile(request):
    return render(request, template_name='subscribed_user/sub_profile.html')
def rented_books(request):
    return render(request, template_name='subscribed_user/rented_books.html')
def sub_navbar(request):
    return render(request, template_name='subscribed_user/sub_navbar.html')
def sub_base(request):
    return render(request, template_name='subscribed_user/sub_base.html')


def log_base(request):
    return render(request, template_name='login_user/log_base.html')
def log_books(request):
    return render(request, template_name='login_user/log_books.html')
def log_help(request):
    return render(request, template_name='login_user/log_help.html')
def log_navbar(request):
    return render(request, template_name='login_user/log_navbar.html')
def log_profile(request):
    return render(request, template_name='login_user/log_profile.html')