import unittest
#from FuelRatePredSys import registration
from django.test import TestCase
from FuelRatePredSys.forms import RegisterForm
# Create your tests here.


class TestRegistrationForm(TestCase):
  
	def test_registration_form_valid_data(self):

	    #test valid data
	    valid_data = {
	      "username": "sam1",
		  "first_name" : "sam", 
		  "last_name" : "sammy",
		  "email" : "sammy@gmail.com",
		  "phone" : "12345678",
		  "city" : "Houston",
		  "state" : "Tx",
		  "password1" : "asdflkj12",
		  "password2" : "asdflkj12"
	    }
	    form = RegisterForm(data=valid_data)
	    form.is_valid()
	    self.assertFalse(form.errors)



