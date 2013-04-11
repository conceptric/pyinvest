import unittest

def cost_of_equity(risk_free, market_risk, stock_beta=1):
    '''
    Calculates the fractional cost of equity given:
    risk_free  : fractional risk free rate.
    market_risk: fractional market risk premimum.
    stock_beta : the market beta of the stock.
    '''
    return round(risk_free + (stock_beta * market_risk), 3)
    
def get_discounting_factors(drate, duration):
    '''
    Returns a list of discounting factors, but it is also 
    applicable to compounding rates, or anything of the form:
    
    (1 + discount rate)^year
    
    drate   : fractional discounting / compounding rate.
    duration: number of years for which factors are required.
    '''
    return map(lambda t: (1 + drate)**t, range(1, duration + 1, 1))



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