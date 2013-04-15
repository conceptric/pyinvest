from pyinvest.utils import *

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
    roe = np.array(roe).astype(float)
    ones = np.ones_like(roe)
    return selective_round((ones - payout_ratio(eps, dps)) * roe, places)
    
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
    
    
def high_growth_phase_value(coe, dps, rate, period):
    '''
    Calculates the stock value of high growth phase.
    coe     : cost of equity (can be a list of values).
    dps     : baseline dividend per share.
    rate    : expected dividend growth rate.
    period  : length of the high growth phase in years.
    Returns the share value of the high growth phase.
    '''
    dividends = get_projected_dividends(dps, rate, years=period)
    coes = get_discounting_factors(coe, period)
    return np.sum(dividends / coes)


