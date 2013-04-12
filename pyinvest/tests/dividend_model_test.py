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
        
class TestDividendGrowthRate(unittest.TestCase):
    """
    Test calculating the dividend growth rate.
    """
    def test_payout_ratio(self):
        actual = get_payout_ratio(313, 219)
        self.assertEquals(actual, 0.6997)
        
    def test_get_growth_rate(self):
        actual = get_growth_rate(313, 219, 0.1163)
        self.assertEquals(actual, 0.0349)

class TestGordonGrowthModel(unittest.TestCase):
    """
    Test valuation using the Gordon Growth Model.
    """
    def test_gordon_growth(self):
        dividend = 1
        cost_of_equity = 0.1
        growth_rate = 0.05
        actual = gordon_growth(dividend, cost_of_equity, growth_rate)
        self.assertEquals(actual[0], 21)

    def test_gordon_growth_with_list_coe(self):
        ''' Returns a list of valuations given a list of costs of equity '''
        dividend = 1
        cost_of_equity = [0.08, 0.1, 0.12]
        growth_rate = 0.05
        actual = gordon_growth(dividend, cost_of_equity, growth_rate)
        self.assertEqual(len(actual), 3)
        self.assertEquals(actual[0], 35)
        self.assertEquals(actual[1], 21)
        self.assertEquals(actual[2], 15)

    def test_gordon_growth_with_list_growth_rates(self):
        ''' Returns a list of valuations given a list of growth rates '''
        dividend = 1
        cost_of_equity = 0.15
        growth_rate = [0.05, 0.075, 0.1]
        actual = gordon_growth(dividend, cost_of_equity, growth_rate)
        self.assertEquals(actual[0], 10.5)
        self.assertEquals(actual[1], 14)
        self.assertEquals(actual[2], 21)

    def test_gordon_growth_with_lists_for_both(self):
        ''' Returns a list of valuations given lists of coe and growth rates '''
        dividend = 1
        cost_of_equity = [0.1, 0.15, 0.2]
        growth_rate = [0.05, 0.1, 0.15]
        actual = gordon_growth(dividend, cost_of_equity, growth_rate)
        self.assertEqual(len(actual), 3)
        for value in actual:
            self.assertEquals(value, 21)
