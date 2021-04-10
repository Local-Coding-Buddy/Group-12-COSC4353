import unittest
from django.test import TestCase
from FuelRatePredSys.forms import FuelQuoteHistory



class TestPriciModule(TestCase):
  
	def test_get_quote_valid_data(self):

	    valid_data = {
		  "gallons_requested" : "1000",
		  "delivery_date" : "05-30-2020",
		  "delivery_address" : "Texas" 
	    }
	    form = FuelQuoteHistory(data=valid_data)
	    form.is_valid()
	    self.assertTrue(form.errors)