from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("home/", views.home, name='home'),
    path("login/", views.login, name='login'),
    path("register/", views.register, name='register'),
    path("profile/",views.profile, name ='profile'),
    path("profile_mangement/",views.profile_mangement, name ='profile_mangement'),

]