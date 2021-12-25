import unittest

from django.test import TestCase
from FuelRatePredSys.forms import EditProfileForm
# Create your tests here.


class TestEditProfileForm(TestCase):
  
	def test_registration_form_valid(self):

	    #test valid data
	    valid_data = {
		  
		  "fullname" : "Manny",
		  "address" : "2312 Cullen St",
		  "city" : "Houston",
		  "state" : "OTHERS",
		  "zipcode" : "77077"
	    }
	    form = EditProfileForm(data=valid_data)
	    form.is_valid()
	    self.assertFalse(form.errors)



