import unittest

from pyinvest.dividend_model import *


class TestStockDividendCover(unittest.TestCase):
    """
    Test calculating the dividend cover.
    """
    def test_payout_ratio_with_integers(self):
        actual = Stock(eps=2, dps=1).dividend_cover()
        self.assertEquals(actual, 2)

    def test_payout_ratio_with_lists(self):
        ratios = Stock(eps=[2, 2], dps=[1, 1]).dividend_cover()
        for ratio in ratios:
            self.assertEquals(ratio, 2)


class TestStockPayoutRatio(unittest.TestCase):
    """
    Test calculating the dividend payout ratio.
    """
    def test_payout_ratio_with_integers(self):
        actual = Stock(eps=313, dps=219).payout_ratio()
        self.assertEquals(actual, 0.69968051118210861)

    def test_payout_ratio_with_lists(self):
        ratios = Stock(eps=[313, 313], dps=[219, 219]).payout_ratio()
        for ratio in ratios:
            self.assertEquals(ratio, 0.69968051118210861)


class TestStockRetentionRatio(unittest.TestCase):
    """
    Test the calculation for stock retention ratio.
    """
    def test_returns_scalar_with_scalar_arguments(self):
        actual = Stock(2, 1).retention_ratio()
        self.assertEquals(actual, 2)

    def test_does_not_truncate_float_solutions(self):
        actual = Stock(2.3, 1.5).retention_ratio()
        self.assertEquals(actual, 1.5333333333333332)
        
    def test_returns_array_with_array_arguments(self):
        ' Returns a solution for each value in the eps array '
        actual = Stock([1, 1], [1, 1]).retention_ratio()
        self.assertEquals(len(actual), 2)
        self.assertIsInstance(actual, np.ndarray)
        for value in actual: self.assertEquals(value, 1)

    def test_with_eps_array_dps_scalar(self):
        actual = Stock([4, 8], 2).retention_ratio()
        self.assertEquals(actual[0], 2)
        self.assertEquals(actual[1], 4)

    def test_with_dps_array_eps_scalar(self):
        actual = Stock(8, [2, 4]).retention_ratio()
        self.assertEquals(actual[0], 4)
        self.assertEquals(actual[1], 2)

class TestStockDividendGrowthRate(unittest.TestCase):
    """
    Test calculating the dividend growth rate.
    """        
    def setUp(self):
        self.eps = 313
        self.dps = 219
        self.roe = 0.1163
        self.expected = 0.03492715654952077
    
    def test_get_growth_rate(self):
        actual = Stock(self.eps, self.dps, self.roe).growth_rate()
        self.assertEquals(actual, self.expected)

    def test_get_growth_rate_with_lists(self):
        eps = [self.eps, self.eps]
        dps = [self.dps, self.dps]
        roe = [self.roe, self.roe]
        for rate in Stock(eps, dps, roe).growth_rate():
            self.assertEquals(rate, self.expected)


if __name__ == '__main__':
    unittest.main()