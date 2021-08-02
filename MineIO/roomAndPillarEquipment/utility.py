import pandas as pd


class utility_att:
    def __init__(self):
        df = pd.read_excel(r'../data/mine_attributes.xlsx', sheet_name="utility", skiprows=1)
        df.set_index('key', inplace=True)
        self.water = df['value'].loc['water']
        self.electricity = df['value'].loc['electricity']
        return



