import pandas as pd

class ColumnExtractionWashing(object):
    def __init__(self):
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name='washing', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.H2O_washing = self.df['value'].loc['H2O_washing']  #l
        self.NaCl_conc = self.df['value'].loc['NaCl_conc']  # g/L
        self.no_washing_cycles = self.df['value'].loc['No_washing_cycles']
        self.stirring_time = self.df['value'].loc['stirring_time']
        self.mass_NaCl = self.H2O_washing * self.NaCl_conc
        self.H2O_washing_total = self.H2O_washing * self.no_washing_cycles
        self.total_mass_NaCl = self.mass_NaCl * self.no_washing_cycles
        return

if __name__ == '__main__':
    test = ColumnExtractionWashing()
    print(test)

