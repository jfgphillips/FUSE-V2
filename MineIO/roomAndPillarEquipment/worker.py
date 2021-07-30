import pandas as pd

class worker_att(object):
    def __init__(self):
        df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="worker", skiprows=1)
        df.set_index('key', inplace=True)
        self.wage = df['value'].loc['wage']
        self.shift_length = df['value'].loc['shift length']
        return
