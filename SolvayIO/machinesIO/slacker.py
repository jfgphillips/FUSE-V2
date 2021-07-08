import pandas as pd


class slacker_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'data/solvay_attributes.xlsx', sheet_name="slacker", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.temperature = self.df['value'].loc['temperature']
        self.time = self.df['value'].loc['residence time']
        return
