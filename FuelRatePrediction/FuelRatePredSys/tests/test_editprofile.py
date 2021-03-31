import unittest

from django.test import TestCase
from FuelRatePredSys.forms import EditProfileForm
# Create your tests here.


class TestEditProfileForm(TestCase):

    def test_registration_form(self):
        # test invalid data
        invalid_data = {
          "email" : "",
          "first_name" : "",
          "last_name" : ""

        }
        form = EditProfileForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

        #test valid data
        valid_data = {

          "fullname" : "Imtiaz",
          "address" : "2111 Holly Hall",
          "city" : "Houston",
          "state" : "OTHERS",
          "zipcode" : "77045"
        }
        form = EditProfileForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)