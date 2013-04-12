import numpy as np

def cost_of_equity(rfr, mrp, beta=1):
    '''
    Calculates the fractional cost of equity from collections:
    
    risk_free  : collection of fractional risk free rates.
    market_risk: collection of fractional market risk premimums.
    stock_beta : collection of the market beta of the stocks.
    
    The beta is optional and defaults to 1.
    Returns the type of the most complex argument.
    '''
    coes = np.array(rfr) + (np.array(beta) * np.array(mrp))
    return selective_round(coes, 3)

def get_discounting_factors(drate, duration=1, places=3):
    '''
    Returns a numpy array of discounting factors, but it is also 
    applicable to compounding rates, or anything of the form:
    
    (1 + rate)^year
    
    drate   : fractional discounting / compounding rate.
              It can be a single value or a list of values 
              for each year.
    duration: number of years for which factors are required.
    places  : number of decimal place for the factors.
    '''
    years = range(1, duration + 1, 1)
    try:
        __check_list_length(drate, duration)
        discounts = map(lambda r, t: (1 + r)**t, drate, years)
    except TypeError:
        discounts = map(lambda t: (1 + drate)**t, years)
    return np.array(selective_round(discounts, places))

def __check_list_length(alist, size):
    ''' Checks the size of a list and raises error incorrect '''
    if len(alist) < size: raise ValueError('List too short.')
    if len(alist) > size: raise ValueError('List too long.')

def selective_round(value, places):
    ''' 
    Applies the round function depending on data type 
    value   : a single or collection of float values.
    places  : an integer for the number of decimal places.
    '''
    try:
        return map(lambda f: round(f, places), value)
    except TypeError:
        return round(value, places)

