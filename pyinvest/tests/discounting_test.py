import unittest

from pyinvest.utils import *

class TestGetDiscountingFactors(unittest.TestCase):
    '''
    Test with optional arguments.
    '''
    def test_returns_a_list(self):
        ''' Returns a list even for a single year '''
        actual = get_discounting_factors(1, 1)
        self.assertIsInstance(actual, list)

    def test_duration_is_optional(self):
        ''' Duration is optional and defaults a single year '''
        actual = get_discounting_factors(1)
        self.assertEquals(len(actual), 1)
        self.assertEquals(actual[0], 2)


class TestDiscountWithFixedRate(unittest.TestCase):
    '''
    Test discounting factors with a fixed discount rate.
    '''
    def setUp(self):
        self.actual = get_discounting_factors(0.04, 5)
        
    def test_correct_length_of_list(self):
        ''' Returns an element for each year '''
        self.assertEquals(len(self.actual), 5)

    def test_with_constant_discount_rate(self):
        ''' 
        Returns correct multi-year results with 
        a constant discount rate.
        '''
        expected = [1.040, 1.082, 1.125, 1.170, 1.217]
        self.assertEquals(self.actual, expected)


class TestDiscountWithVariableRates(unittest.TestCase):
    '''
    Test discounting factors with a variable discount rate.
    '''
    def setUp(self):
        rates = [0.01, 0.02, 0.04, 0.08, 0.16]
        self.actual = get_discounting_factors(rates, 5)
        
    def test_correct_length_of_list(self):
        ''' Returns an element for each year '''
        self.assertEquals(len(self.actual), 5)

    def test_with_constant_discount_rate(self):
        ''' 
        Returns correct multi-year results with 
        a constant discount rate.
        '''
        expected = [1.010, 1.040, 1.125, 1.360, 2.100]
        self.assertEquals(self.actual, expected)



if __name__ == '__main__':
    unittest.main()