from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views


#app_name = "FQ"
urlpatterns = [
    path("", views.index, name='index'),
    path("home/", views.home, name='home'),
    path("register/", views.register, name='register'),
    path("profile/",views.profile, name ='profile'),
    path("profile_management/",views.profile_management, name ='profile_management'),
    path('fqh/', views.quote_history, name='FuelRatePredSys-fqh'),
    path('fqf/', views.quote_form, name='FuelRatePredSys-fqf'),
    path('receipt/', views.receipt, name='receipt'),

]