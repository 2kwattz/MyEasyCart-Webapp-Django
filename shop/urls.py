
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from shop.views import custom_404_view
from .views import UserRegistrationView, UserProfileView, UserLoginView
from . import views

urlpatterns = [
    path('', views.index, name="shopIndex"),
    path('about/', views.about, name="shopAbout"),
    path('tracker/', views.tracker, name="shopTracker"),
    path('search/', views.search, name="shopSearch"),
    path('productview', views.productView, name="shopProductView"),
    path('checkout/', views.checkout, name="shopCheckout"),
    path('login/', views.login, name="shopLogin"),
    path('login2/', UserLoginView.as_view(), name="shopLogin2"),
    path('contact/', views.contact, name="shopContact"),
    path('products/', views.products, name="shopProducts"),
    path('api/contacts/', views.contact_api, name='contact_api'),
    path('contactdata/', views.contactData, name='contactData'),
    path('registration/', views.registration, name="shopRegistration"),
    path('register/', UserRegistrationView.as_view(), name="shopRegister" ),
    path('userprofile/', UserProfileView.as_view(), name="shopProfile" ),
    path('jsoneg/', views.jsoneg, name="jsonEg")

]

handler404 = 'shop.views.custom_404_view'
