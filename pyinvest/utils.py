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
    
def get_discounting_factors(drate, duration=1):
    '''
    Returns a list of discounting factors, but it is also 
    applicable to compounding rates, or anything of the form:
    
    (1 + discount rate)^year
    
    drate   : fractional discounting / compounding rate.
    duration: number of years for which factors are required.
    '''
    years = range(1, duration + 1, 1)
    rates = np.array(drate)
    try:
        discounts = map(lambda r, t: (1 + r)**t, rates, years)
    except TypeError:
        discounts = map(lambda t: (1 + drate)**t, years)
    return selective_round(discounts, 3)



