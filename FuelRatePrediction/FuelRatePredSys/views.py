from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserProfileFrom, EditProfileForm, FuelHistoryPage, FuelQuoteHistory 
import logging
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



def quote_form(request):
	history_list1 = Pricing_Module.objects.filter(user=request.user)
	if request.method == 'POST':
		form = FuelQuoteHistory(request.POST)
		if form.is_valid():
			form.save(commit=False)
			form.instance.user = request.user
			form.save()
			args = {"form":form, "history_list1":history_list1}
			return render(request, 'FuelRatePredSys/quote_form.html', args )
	else:
		form = FuelQuoteHistory()
	return render(request, 'FuelRatePredSys/quote_form.html', {"form":form, "history_list1":history_list1})

def quote_history(request):
	form = FuelHistoryPage()
	history_list = Pricing_Module.objects.filter(user=request.user)
	args ={'history_list': history_list}
	return render(request, 'FuelRatePredSys/quote_history.html', args)


def profile(request):
    args = {'user': request.user}
    return render(request, 'FuelRatePredSys/profile.html', args)
	
def profile_management(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance=request.user)
        p_form = EditProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
            return redirect('/profile')

    else:
        form = EditProfileForm(instance=request.user)
        p_form = EditProfileForm(request.POST, instance=request.user.userprofile)
        args = {'form':form, 'p_form':p_form}
        return render(request, 'FuelRatePredSys/profile_management.html', args)

