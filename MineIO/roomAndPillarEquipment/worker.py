import pandas as pd

class worker_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="worker", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.wage = self.df['value'].loc['wage']
        self.shift_length = self.df['value'].loc['shift length']
        return
