import unittest

from pyinvest.dividend_model import *

class TestProjectedDividends(unittest.TestCase):
    """
    Test Dividend Growth Model functions
    """
    def test_returns_next_year_dividend(self):
        actual = get_projected_dividends(1, 0.05)
        self.assertEquals(actual, [1.05])
        
    def test_returns_next_two_years_dividends(self):
        actual = get_projected_dividends(1, 0.05, 2)
        self.assertEquals(actual, [1.05, 1.1025])    