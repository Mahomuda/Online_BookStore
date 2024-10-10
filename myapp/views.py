from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, template_name='bmHome/home.html')
def books (request):
    return render(request, template_name='bmHome/books.html')
def contacts(request):
    return render(request, template_name='bmHome/contacts.html')
def litshelf(request):
    return render(request, template_name='bmHome/litshelf.html')


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
    return render(request, template_name='login_signup_subscription/login.html')
def signup(request):
    return render(request, template_name='login_signup_subscription/signup.html')
def subscription(request):
    return render(request, template_name='login_signup_subscription/subscription.html')
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


