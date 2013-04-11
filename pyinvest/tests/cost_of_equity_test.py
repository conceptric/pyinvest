import unittest

from pyinvest.utils import *

class TestCostOfEquityWithScalars(unittest.TestCase):
    """
    The Cost of Equity function with single value 
    arguments.
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


class TestCostOfEquityWithSingleElementArrays(unittest.TestCase):
    """
    The Cost of Equity function with single element 
    array arguments.
    """
    def test_no_beta_supplied(self):
        ''' Optional beta defaults to 1 '''
        actual = cost_of_equity([1], [1])
        self.assertEquals(actual, [2])

    def test_beta_equals_scalar_zero(self):
        actual = cost_of_equity([1], [1], 0)
        self.assertEquals(actual, [1])


class TestCostOfEquityWithMultlElementArrays(unittest.TestCase):
    """
    The Cost of Equity function with multiple element 
    array arguments.
    """
    def setUp(self):
        self.risk = [1, 1]
        self.market = [1, 1]

    def test_no_beta_supplied(self):
        ''' Optional beta defaults to 1 '''
        actual = cost_of_equity(self.risk, self.market)
        self.assertEquals(actual[0], 2)
        self.assertEquals(actual[1], 2)

    def test_two_dimension_arguments(self):
        betas = [0, 1]
        actual = cost_of_equity(self.risk, self.market, betas)
        self.assertEquals(actual[0], 1)
        self.assertEquals(actual[1], 2)

    def test_two_dimension_arguments_with_rounding(self):
        betas = [0.55550, 0.55551]
        actual = cost_of_equity(self.risk, self.market, betas)
        self.assertEquals(actual[0], 1.555)
        self.assertEquals(actual[1], 1.556)


        
if __name__ == '__main__':
    unittest.main()