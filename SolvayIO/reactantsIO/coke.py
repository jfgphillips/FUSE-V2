import pandas as pd
from molmass import Formula


class coke_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'data/solvay_attributes.xlsx', sheet_name="coke", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.coke_mol = self.df['value'].loc['mass'] / Formula("C").mass
        self.coke_price = self.df['value'].loc['price']
        return

