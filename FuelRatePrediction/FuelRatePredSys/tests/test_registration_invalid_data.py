import unittest
#from FuelRatePredSys import registration
from django.test import TestCase
from FuelRatePredSys.forms import RegisterForm
# Create your tests here.


class TestRegistrationForm(TestCase):
  
	def test_registration_form_invalid_data(self):
    	# test invalid data
	    invalid_data = {
	      "username": "",
		  "first_name" : "",
		  "last_name" : "",
		  "email" : "",
		  "phone" : "",
		  "city" : "",
		  "state" : "",
		  "password1" : "",
		  "password2" : ""
	    }
	    form = RegisterForm(data=invalid_data)
	    form.is_valid()
	    self.assertTrue(form.errors)



