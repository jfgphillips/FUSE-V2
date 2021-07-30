import pandas as pd


class longwallShearer_att:
    def __init__(self):
        df= pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="longwall shearer", skiprows=1)
