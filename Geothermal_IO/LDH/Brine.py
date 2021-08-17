import pandas as pd


class Brine_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'\Users\chant\PycharmProjects\FUSE-V2\data\LDH_attributes.xlsx',
                                sheet_name='brine', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.Li_conc_brine = self.df['value'].loc['LiCl_conc_brine']
        self.brine_specific_enthalpy = self.df['value'].loc['brine_specific_enthalpy']
        self.brine_density = self.df['value'].loc['brine_density']
        return
