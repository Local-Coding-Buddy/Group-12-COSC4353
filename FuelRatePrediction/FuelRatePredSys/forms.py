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

