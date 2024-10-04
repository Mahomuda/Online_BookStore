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