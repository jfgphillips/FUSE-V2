import pandas as pd
from calculators import unitConversions


class limestone_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/solvay_attributes.xlsx', sheet_name="limestone", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.CaCO3_mass = self.df['value'].loc['mass']
        self.CaCO3_mol = unitConversions.solidMol("CaCO3", self.CaCO3_mass)
        self.CaCO3_price = self.df['value'].loc['price']
        return
