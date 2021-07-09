import pandas as pd
from calculators import unitConversions


class brine_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/solvay_attributes.xlsx', sheet_name="brine", skiprows=1)
        self.df.set_index('formula', inplace=True)
        self.NaCl_mass = self.df['value'].loc['NaCl']
        self.NaCl_mol = unitConversions.solidMol("NaCl", self.NaCl_mass)

        return
