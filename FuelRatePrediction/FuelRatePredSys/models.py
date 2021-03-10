from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	STATE = (('TX', 'Texas'),('OTHERS', 'Out of Texas'))
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=100, default='')
	address = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=20, default='')
	state = models.CharField(max_length=20, choices=STATE)
	zipcode = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username

class Fuel_Quote(models.Model):
	userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	gallons = models.IntegerField(default=0)
	delivery_date = models.DateField(auto_now=False,auto_now_add=False)
	delivery_address = models.CharField(default='', max_length=100)
	s_price = models.DecimalField(max_digits=10,decimal_places=2)
	t_price = models.DecimalField(max_digits=10,decimal_places=2)
	
	def __str__(self):
		return self.t_price

