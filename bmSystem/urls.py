"""
URL configuration for bmSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf import settings
from django.conf.urls.static import static

from myapp import views as myapp_views
from myapp import views as buy_books_views
from myapp import views as login_signup_subscription
from myapp import views as login_user
from myapp import views as subscribed_user
from myapp import views as rent_books
from myapp import views as shop
from myapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',myapp_views.home, name='home'),
    path('contacts/',myapp_views.contacts, name='contacts'),
    path('books/',myapp_views.books, name='books'),
    path('',myapp_views.litshelf, name='litshelf'),
    path('books/<int:book_id>/', views.books_details, name='books_details'), 


    #path('academic/', buy_books_views.academic, name='academic'),
    #path('Buy_Books/<int:book_id>',buy_books_views.books_details, name = 'books_details'),
    #path('upload_Books/', buy_books_views.upload_Books, name='upload_Books'),
    #path('books_details/<int:book_id>', buy_books_views.books_details, name='books_details'),


    path('login/', login_signup_subscription.login, name='login'),
    path('signup/', login_signup_subscription.signup, name='signup'),
    path('subscription/', login_signup_subscription.subscription, name='subscription'),
    path('forget_pass/', login_signup_subscription.forget_pass, name='forget_pass'),
    path('login_with/', login_signup_subscription.login_with, name='login_with'),
    path('payment/', login_signup_subscription.payment, name='payment'),
    path('process-payment/', login_signup_subscription.process_payment, name='process_payment'),

    path('log_base/', login_user.log_base, name='log_base'),
    path('log_navbar/', login_user.log_navbar, name='log_navbar'),
    path('log_book/', login_user.log_book, name='log_book'),
    path('log_books_details/<int:book_id>', login_user.log_books_details, name='log_books_details'),
    path('log_help/', login_user.log_help, name='log_help'),
    path('log_profile/', login_user.log_profile, name='log_profile'),
    path('purchase_book/<int:book_id>/purchase/', login_user.purchase_book, name='purchase_book'),
    path('confirm_payment/<int:book_id>/', login_user.confirm_payment, name='confirm_payment'),
    path('process-payment/<int:book_id>/', login_user.process_payment_for_book, name='process_payment_for_book'),
    path('payment_confirmation/<int:book_id>/', login_user.payment_confirmation, name='payment_confirmation'),
    


    path('u_help/', subscribed_user.u_help, name='sub_help'),
    path('sub_profile/', subscribed_user.sub_profile, name='sub_profile'),
    path('subscribed_user/sub_base/', subscribed_user.sub_base, name='sub_base'),
    path('sub_navbar/', subscribed_user.sub_navbar, name='sub_navbar'),
     

    path('shop_base/', shop.shop_base, name='shop_base'),
    path('shop_navbar/', shop.shop_navbar, name='shop_navbar'),
    path('shop_book/', shop.shop_books, name='shop_books'),
    path('shop_book_details/<int:book_id>', shop.shop_book_details, name='shop_book_details'),
    path('shop_help/', shop.shop_help, name='shop_help'),
    path('shop_profile/', shop.shop_profile, name='shop_profile'),
    path('shop_payment/', shop.shop_payment, name='shop_payment'),
   
   
    path('sub_profile/<int:user_id>/', views.view_sub_profile, name='view_sub_profile'),
    
   
     # Purchase and Checkout paths
    

]

   

   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



