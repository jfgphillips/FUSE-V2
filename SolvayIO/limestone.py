import pandas as pd
from calculators import unitConversions


class limestone_att(object):
    def __init__(self):
        df = pd.read_excel(r'../data/solvay_attributes.xlsx', sheet_name="limestone", skiprows=1)
        df.set_index('key', inplace=True)
        self.CaCO3_mass = df['value'].loc['mass']
        self.CaCO3_mol = unitConversions.solidMol("CaCO3", self.CaCO3_mass)
        self.CaCO3_price = df['value'].loc['price']
        return
