import unittest

from pyinvest.dividend_model import *

class TestHighGrowthPhase(unittest.TestCase):
    '''
    Test the object representing a stock in the 
    high growth phase of the dividend discount model.
    '''
    def test_exists(self):
        self.assertTrue(HighGrowthPhase(1, 1, 1))

    def test_duration_is_optional_default_to_one(self):
        high_growth = HighGrowthPhase(1, 1, 1)
        self.assertEquals(high_growth.duration, 1)


class TestHighGrowthPhaseValue(unittest.TestCase):
    """
    Test the method used to calculate the high growth 
    phase value.
    """
    def test_it_works_for_a_single_year_of_growth(self):
        value = HighGrowthPhase(coe=0.1, dps=2, rate=0.1).get_value()
        self.assertEquals(value, 2)

    def test_it_works_for_a_two_years_of_growth(self):
        value = HighGrowthPhase(coe=0.1, dps=2, rate=0.1, duration=2).get_value()
        self.assertEquals(value, 4)