import pandas as pd

class ColumnExtractionStripping(object):
    def __init__(self):
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name='stripping', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.H2O_stripping = self.df['value'].loc['H2O_stripping']  #l
        self.no_stripping_cycles = self.df['value'].loc['No_stripping_cycles']
        self.LiCl_conc_stripping = self.df['value'].loc['LiCl_conc_stripping']
        self.LiCl_sol_output = self.df['value'].loc['LiCl_sol_output']
        self.H2O_stripping_total = self.H2O_stripping + self.no_stripping_cycles
        return

if __name__ == '__main__':
    test = ColumnExtractionStripping()
    print(test)