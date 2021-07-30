import pandas as pd
from calculators import unitConversions



class ammonia_att(object):
    def __init__(self):
        df = pd.read_excel(r'../data/solvay_attributes.xlsx', sheet_name="ammonia", skiprows= 1)
        df.set_index('key', inplace=True)
        self.NH3_mass = df['value'].loc['mass']
        self.NH3_mol = unitConversions.solidMol("NH3", self.NH3_mass)
        self.NH3_price = df['value'].loc['price']
        return
