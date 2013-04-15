import numpy as np

class Stock:
    """
    Class to represent the data and ratios of a stock.
    """
    def __init__(self, eps, dps, roe=0):
        '''
        eps: earnings per share.
        dps: dividends per share.        
        roe: fractional return on equity, default to 0.
        '''
        self.eps = np.array(eps).astype(float)
        self.dps = np.array(dps).astype(float)
        self.roe = np.array(roe).astype(float)

    def retention_ratio(self):
        '''
        Calculates the retention ratio for a stock.    
        Returns fractional payout ratio numpy array.
        '''
        return self.eps / self.dps

    def dividend_cover(self):
        '''
        Returns the dividend cover for the stock (alias 
        for retention_ratio).
        '''
        return self.retention_ratio()

    def payout_ratio(self):
        '''
        Calculates the stock payout ratio based on:
        Returns fractional payout ratio numpy array.
        '''
        return 1 / self.retention_ratio()
        
    def growth_rate(self):
        '''
        Calculates the dividend growth rate:
        
        (1 - payout ratio)^cost of equity
                    
        Returns the fractional expected growth rate numpy array.
        '''
        ones = np.ones_like(self.roe)
        return (ones - self.payout_ratio()) * self.roe
        
