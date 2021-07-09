import pandas as pd
from calculators import unitConversions



class ammonia_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/solvay_attributes.xlsx', sheet_name="ammonia", skiprows= 1)
        self.df.set_index('key', inplace=True)
        self.NH3_mass = self.df['value'].loc['mass']
        self.NH3_mol = unitConversions.solidMol("NH3", self.NH3_mass)
        self.NH3_price = self.df['value'].loc['price']
        return
