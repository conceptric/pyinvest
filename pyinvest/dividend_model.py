from pyinvest.utils import *

class Stock:
    """
    Class to represent the data and ratios of a stock.
    """
    def __init__(self, eps, dps):
        '''
        eps: earnings per share.
        dps: dividends per share.        
        '''
        self.eps = np.array(eps).astype(float)
        self.dps = np.array(dps).astype(float)

    def retention_ratio(self):
        '''
        Calculates the retention ratio for a stock:    
        Returns fractional payout ratio numpy array.
        '''
        return self.eps / self.dps

    def payout_ratio(self):
        '''
        Calculates the stock payout ratio based on:
        Returns fractional payout ratio numpy array.
        '''
        return 1 / self.retention_ratio()
            
        
class HighGrowthPhase:
    """
    Class representing a stock in the high growth 
    phase of the dividend discount model.
    coe     : baseline cost of equity (can be a list of values).
    dps     : baseline dividend per share.
    rate    : expected dividend growth rate.
    duration: length of the high growth phase in years.
    """
    def __init__(self, coe, dps, rate, duration=1):
        self.coe = coe
        self.dps = dps
        self.rate= rate
        self.duration = duration
    
    def get_dividends(self):        
        return get_projected_dividends(self.dps, self.rate, years=self.duration)
    
    def get_cost_of_equity(self):
        return get_discounting_factors(self.coe, self.duration)
    
    def get_value(self):
        '''
        Returns the share value of the high growth phase.
        '''
        return np.sum(self.get_dividends() / self.get_cost_of_equity())


def get_projected_dividends(current, rate, years=1, places=4):
    '''
    Calculates the future expected dividends.

    current : current dividend per share.
    rate    : expected dividend growth rates.
    years   : number of years to estimate.
    places  : number of decimal place for the dividends.

    Returns a list of the compounded expected dividends.
    '''
    return current * get_discounting_factors(rate, years, places)

def get_growth_rate(eps, dps, roe, places=4):
    '''
    Calculates the expected growth rate based on:
    
    eps: earnings per share.
    dps: dividends per share.
    roe: fractional return on equity.
    places: optionally defines the decimal rounding, default 4.
    
    Returns the fractional expected growth rate numpy array.
    '''
    stock = Stock(eps, dps)
    roe = np.array(roe).astype(float)
    ones = np.ones_like(roe)
    return selective_round((ones - stock.payout_ratio()) * roe, places)
    
def gordon_growth(current, coe, growth):
    '''
    Calculates the steady state price of the stock 
    based on dividends.
    
    current : current dividend.
    coe     : cost of equity (can be a list of values).
    growth  : expected dividend growth rate 
            (can be a list of values and the base line is the 
            first in the list).
    
    Returns a list of the values of the stock based on the 
    supplied data.
    '''
    try:
        future = get_projected_dividends(current, growth[0])
    except TypeError:
        future = get_projected_dividends(current, growth)
    return selective_round(future / (np.array(coe) - np.array(growth)), 2)
    
