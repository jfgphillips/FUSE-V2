import pandas as pd
from molmass import Formula


class brine_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'data/solvay_attributes.xlsx', sheet_name="brine", skiprows=1)
        self.df.set_index('formula', inplace=True)
        self.NaCl_mol = self.df['value'].loc['NaCl'] / Formula("NaCl").mass
        return
