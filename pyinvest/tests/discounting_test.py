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


class TestGetDiscountingFactors(unittest.TestCase):
    '''
    Test discounting factors with a fixed discount rate.
    '''
    def setUp(self):
        self.actual = get_discounting_factors(1, 5)
        
    def test_correct_length_of_list(self):
        ''' Returns an element for each year '''
        self.assertEquals(len(self.actual), 5)

    def test_with_constant_discount_rate(self):
        ''' 
        Returns correct multi-year results with 
        a constant discount rate.
        '''
        expected = [2, 4, 8, 16, 32]
        self.assertEquals(self.actual, expected)


if __name__ == '__main__':
    unittest.main()