import pandas as pd
from Geothermal_IO.LDH import Plant
from Geothermal_IO.LDH import Brine
from Geothermal_IO.LDH import Column

class ColumnExtractionWashing(object):
    def __init__(self):
        self.plant = Plant.Plant_att()
        self.brine = Brine.Brine_att()
        self.column = Column.Column_att()
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name='washing', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.NaCl_conc = self.df['value'].loc['NaCl_conc']  # g/L
        self.H2O_washing = self.df['value'].loc['H2O_washing']
        self.stirring_time = self.df['value'].loc['stirring_time']  # l
        self.mass_NaCl = self.H2O_washing * self.NaCl_conc  # g
        return

if __name__ == '__main__':
    test = ColumnExtractionWashing()
    print(test)

