import unittest

from pyinvest.utils import *

class TestGetDiscountingFactors(unittest.TestCase):
    '''
    Test a function to return a list of annual discounting factors 
    based on a discounting rate and a duration.
    '''
    def test_length_of_list(self):
        actual = get_discounting_factors(1, 5)
        self.assertEquals(len(actual), 5)

    def test_returned_values_correct(self):
        expected = [2, 4, 8, 16, 32]
        actual = get_discounting_factors(1, 5)
        self.assertEquals(actual, expected)

if __name__ == '__main__':
    unittest.main()