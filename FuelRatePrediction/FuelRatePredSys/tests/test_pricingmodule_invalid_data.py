import unittest
from django.test import TestCase
from FuelRatePredSys.forms import FuelQuoteHistory



class TestPriciModule(TestCase):
  
	def test_get_quote_invalid_data(self):
    	# test invalid data
	    invalid_data = {
		  "gallons_requested" : "",
		  "delivery_date" : "",
		  "delivery_address" : "" 
	    }
	    form = FuelQuoteHistory(data=invalid_data)
	    form.is_valid()
	    self.assertTrue(form.errors)

