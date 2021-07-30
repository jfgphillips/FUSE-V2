import pandas as pd


class stageLoader_att:
    def __init__(self):
        df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="stage loader", skiprows=1)
        df.set_index('key', inplace=True)
        self.power = df['value'].loc['power']
        self.workers = df['value'].loc['workers']
