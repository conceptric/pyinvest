import numpy as np

def cost_of_equity(risk_free, market_risk, stock_beta=1):
    '''
    Calculates the fractional cost of equity given:
    risk_free  : fractional risk free rate.
    market_risk: fractional market risk premimum.
    stock_beta : the market beta of the stock.
    '''
    return round(risk_free + (stock_beta * market_risk), 3)

def array_cost_of_equity(rfr, mrp, beta=1):
    coes = np.array(rfr) + (np.array(beta) * np.array(mrp))
    return map(lambda f: round(f, 3), coes)

    
def get_discounting_factors(drate, duration):
    '''
    Returns a list of discounting factors, but it is also 
    applicable to compounding rates, or anything of the form:
    
    (1 + discount rate)^year
    
    drate   : fractional discounting / compounding rate.
    duration: number of years for which factors are required.
    '''
    return map(lambda t: (1 + drate)**t, range(1, duration + 1, 1))



