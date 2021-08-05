import pandas as pd

class ForwardOsmosis(object):
    def __init__(self):
        self.df = pd.read_excel(r'Users\chant\PycharmProjects\FUSE-V2\data\LDH_attributes.xlsx',
                                sheet_name='FO', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.LiCl_conc_FO = self.df['value'].loc['LiCl_conc_FO']
        self.Li_sol_output = self.df['value'].loc['Li_sol_output']
        