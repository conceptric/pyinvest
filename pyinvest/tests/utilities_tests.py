import unittest
import numpy as np

from pyinvest.utils import *

class TestRetentionRatio(unittest.TestCase):
    """
    Test the calculation for stock retention ratio
    """
    def test_returns_scalar_with_scalar_arguments(self):
        actual = retention_ratio(2, 1)
        self.assertEquals(actual, 2)
        
    def test_returns_array_with_array_arguments(self):
        ' Returns a solution for each value in the eps array '
        actual = retention_ratio([1, 1], [1, 1])
        self.assertEquals(len(actual), 2)
        self.assertIsInstance(actual, np.ndarray)
        for value in actual: self.assertEquals(value, 1)

    def test_with_eps_array_dps_scalar(self):
        actual = retention_ratio([4, 8], 2)
        self.assertEquals(actual[0], 2)
        self.assertEquals(actual[1], 4)

    def test_with_dps_array_eps_scalar(self):
        actual = retention_ratio(8, [2, 4])
        self.assertEquals(actual[0], 4)
        self.assertEquals(actual[1], 2)


if __name__ == '__main__':
    unittest.main()