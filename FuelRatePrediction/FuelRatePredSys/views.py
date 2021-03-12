from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserProfileFrom, EditProfileForm

from .models import UserProfile, Pricing_Module

def index(request):
	return render(request, 'FuelRatePredSys/home.html')

def home(request):
	 return render(request, 'FuelRatePredSys/home.html')

def loginHome(request):
	return render(request, 'FuelRatePredSys/loginHome.html')

@login_required
def go_home_page(request):
	product = get_object_or_404(UserProfile)
	return render(request, 'FuelRatePredSys/loginHome.html', {'product' : product})

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		profile_form = UserProfileFrom(request.POST)

		if form.is_valid() and profile_form.is_valid():
			user = form.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			
			return redirect("/home")
	else:
		form = RegisterForm()
		profile_form= UserProfileFrom()
	args = {"form":form, "profile_form":profile_form}
	return render(request, "FuelRatePredSys/register.html", args)

def profile(request):
	args = {'user': request.user}
	return render(request, 'FuelRatePredSys/profile.html', args)



def quote_form(request):#, user_id):
	#uid = get_object_or_404(UserProfile, pk=user_id)
	return render(request, 'FuelRatePredSys/quote_form.html')

def quote_history(request,):
	#uid = get_object_or_404(UserProfile, pk=user_id)
	return render(request, 'FuelRatePredSys/quote_history.html')
	
