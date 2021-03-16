from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
from django.forms import ModelForm

from .models import UserProfile, Pricing_Module

class RegisterForm(UserCreationForm):

	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ('username', 'email','password1', 'password2')

	def save(self, commit=True):
		user = super().save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class UserProfileFrom(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('fullname', 'address', 'city', 'state', 'zipcode')


class EditProfileForm(UserChangeForm):
	class Meta:
		model = UserProfile
		fields = ('fullname', 'address', 'city', 'state', 'zipcode')


class QuoteHistory(forms.ModelForm):
	class Meta:
		model = Pricing_Module
		fields = ('gallons','delivery_date','delivery_address','s_price','t_price')
		# gallons = forms.IntegerField()
		# delivery_date = forms.DateField()
		# delivery_address = forms.CharField(max_length=100)
		# s_price = forms.DecimalField(max_digits=10,decimal_places=2)
		# t_price = forms.DecimalField(max_digits=10,decimal_places=2)

class Quote(forms.ModelForm):
	class Meta:
		model = Pricing_Module
		fields = ('gallons','delivery_date')
		# gallons = forms.IntegerField(label = 'Number of Gallons')
		# delivery_date = forms.DateField()
		# delivery_address = forms.CharField(max_length=100)

