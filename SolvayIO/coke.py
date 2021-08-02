import pandas as pd
from calculators import unitConversions


class coke_att(object):
    def __init__(self):
        df = pd.read_excel(r'../data/solvay_attributes.xlsx', sheet_name="coke", skiprows=1)
        df.set_index('key', inplace=True)
        self.coke_mass = df['value'].loc['mass']
        self.coke_mol = unitConversions.solidMol("C", self.coke_mass)
        self.coke_price = df['value'].loc['price']
        return

