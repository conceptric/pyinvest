import unittest
import numpy as np

from pyinvest.dividend_model import *

class TestHighGrowthValue(unittest.TestCase):
    """
    Test the functions used to calculate the high growth 
    phase value.
    """
    def test_it_works_for_a_single_year_of_growth(self):
        value = high_growth_phase_value(0.1, 2, 0.1, period=1)
        self.assertEquals(value, 2)
        
    def test_it_works_for_a_two_years_of_growth(self):
        value = high_growth_phase_value(0.1, 2, 0.1, period=2)
        self.assertEquals(value, 4)