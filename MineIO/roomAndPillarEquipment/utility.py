import pandas as pd


class utility_att:
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="utility", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.water = self.df['value'].loc['water']
        self.electricity = self.df['value'].loc['electricity']
        return



