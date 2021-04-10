import unittest

from django.test import TestCase
from FuelRatePredSys.forms import EditProfileForm
# Create your tests here.


class TestEditProfileForm(TestCase):
  
	def test_registration_form_invalid(self):
    	# test invalid data
	    invalid_data = {
		  "email" : "",
		  "first_name" : "",
		  "last_name" : ""

	    }
	    form = EditProfileForm(data=invalid_data)
	    form.is_valid()
	    self.assertTrue(form.errors)
	
	


