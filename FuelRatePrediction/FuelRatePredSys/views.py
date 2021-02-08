from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def index(request):
	return render(request, 'FuelRatePredSys/home.html')

def home(request):
	 return render(request, 'FuelRatePredSys/home.html')

def login(request):
	return render(request, 'FuelRatePredSys/login.html')

def register(request):
	return render(request, 'FuelRatePredSys/register.html')

def profile(request):
	return render(request, 'FuelRatePredSys/profile.html')
