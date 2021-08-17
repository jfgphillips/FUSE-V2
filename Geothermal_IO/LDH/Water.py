import pandas as pd

class Water_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'\Users\chant\PycharmProjects\FUSE-V2\data\LDH_attributes.xlsx',
                                sheet_name='water', skiprows=1)
        self.df.set_index('key', inplace=True),
        self.sor_syn_washing = self.df['value'].loc['sor_syn_washing']
        self.LC_purification_washing = self.df['value'].loc['LC_purification_washing']