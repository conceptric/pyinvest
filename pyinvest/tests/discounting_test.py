import unittest
import numpy as np

from pyinvest.utils import *

class TestGetDiscountingFactors(unittest.TestCase):
    '''
    Test with optional arguments.
    '''
    def test_returns_an_array(self):
        ''' Returns a numpy array even for a single year '''
        actual = get_discounting_factors(1, 1)
        self.assertIsInstance(actual, np.ndarray)

    def test_duration_is_optional(self):
        ''' Duration is optional and defaults a single year '''
        actual = get_discounting_factors(1)
        self.assertEquals(len(actual), 1)
        self.assertEquals(actual[0], 2)

    def test_decimal_places_in_factors(self):
        ''' Places is optional and defaults to 3 decimal places '''
        actual = get_discounting_factors(1.1111)
        self.assertEquals(actual[0], 2.111)

    def test_decimal_places_can_be_specified(self):
        actual = get_discounting_factors(1.1111, places=4)
        self.assertEquals(actual[0], 2.1111)


class TestDiscountWithFixedRate(unittest.TestCase):
    '''
    Test discounting factors with a fixed discount rate.
    '''
    def setUp(self):
        self.actual = get_discounting_factors(0.04, 5)
        
    def test_correct_length_of_array(self):
        ''' Returns an element for each year '''
        self.assertEquals(len(self.actual), 5)

    def test_with_constant_discount_rate(self):
        ''' 
        Returns correct multi-year results with 
        a constant discount rate.
        '''
        expected = [1.040, 1.082, 1.125, 1.170, 1.217]
        for i in range(0, len(expected), 1):
            self.assertEquals(self.actual[i], expected[i])


class TestDiscountWithVariableRates(unittest.TestCase):
    '''
    Test discounting factors with a variable discount rate.
    '''
    def setUp(self):
        self.rates = [0.01, 0.02, 0.04, 0.08, 0.16]
        self.years = len(self.rates)
        self.actual = get_discounting_factors(self.rates, self.years)
        
    def test_correct_length_of_array(self):
        ''' Returns an element for each year '''
        self.assertEquals(len(self.actual), self.years)

    def test_with_constant_discount_rate(self):
        ''' 
        Returns correct multi-year results with 
        a constant discount rate.
        '''
        expected = [1.010, 1.040, 1.125, 1.360, 2.100]
        for i in range(0, len(expected), 1):
            self.assertEquals(self.actual[i], expected[i])

    def test_must_have_a_rate_for_each_year(self):
        ''' 
        Raise an error if rate list length is too short.
        '''
        self.rates.pop()
        self.assertEquals(len(self.rates), self.years - 1)
        with self.assertRaises(ValueError):
            get_discounting_factors(self.rates, self.years)

    def test_must_only_have_a_rate_for_each_year(self):
        ''' 
        Raise an error if rate list length is too long.
        '''
        self.rates.append(0.01)
        self.assertEquals(len(self.rates), self.years + 1)
        with self.assertRaises(ValueError):
            get_discounting_factors(self.rates, self.years)
        
        
if __name__ == '__main__':
    unittest.main()