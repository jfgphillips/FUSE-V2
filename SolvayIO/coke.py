import pandas as pd
from calculators import unitConversions


class coke_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/solvay_attributes.xlsx', sheet_name="coke", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.coke_mass = self.df['value'].loc['mass']
        self.coke_mol = unitConversions.solidMol("C", self.coke_mass)
        self.coke_price = self.df['value'].loc['price']
        return

