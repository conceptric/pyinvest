import unittest

from pyinvest.utils import *

class TestCostOfEquity(unittest.TestCase):
    """
    Testing basic dividend discount model functions.
    """
    def test_when_beta_is_zero(self):
        actual = cost_of_equity(1, 1, 0)
        self.assertEquals(actual, 1)

    def test_beta_optional_and_equals_one(self):
        actual = cost_of_equity(1, 1)
        self.assertEquals(actual, 2)

    def test_realistic_arguments(self):
        actual = cost_of_equity(0.04, 0.05, 0.8)
        self.assertEquals(actual, 0.08)

    def test_rounds_to_three_decimal_places(self):
        actual = cost_of_equity(0.04, 0.03, 0.33)
        self.assertEquals(actual, 0.05)

        
if __name__ == '__main__':
    unittest.main()