import pandas as pd

class ForwardOsmosis(object):
    def __init__(self):
        self.df = pd.read_excel(r'..\..\data\LDH_attributes.xlsx',
                                sheet_name='FO', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.LiCl_conc_FO = self.df['value'].loc['LiCl_conc_FO']
        self.LiCl_sol_output = self.df['value'].loc['LiCl_sol_output']
        self.efficiency = self.df['value'].loc['efficiency']

if __name__ == '__main__':
    test = ForwardOsmosis()
    print(test)