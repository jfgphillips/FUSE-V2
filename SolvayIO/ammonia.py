import pandas as pd
from molmass import Formula


class ammonia_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/solvay_attributes.xlsx', sheet_name="ammonia", skiprows= 1)
        self.df.set_index('key', inplace=True)
        self.NH3_mol = self.df['value'].loc['mass']/Formula("NH3").mass
        self.NH3_price = self.df['value'].loc['price']
        print(self.NH3_mol)
        return
