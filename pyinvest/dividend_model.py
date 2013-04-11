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
