import pandas as pd
from Geothermal_IO.LDH import Plant
from Geothermal_IO.LDH import Column

class ColumnExtractionStripping(object):
    def __init__(self):
        self.plant = Plant.Plant_att()
        self.column = Column.Column_att()
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name='stripping', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.LiCl_conc_stripping = self.df['value'].loc['LiCl_conc_stripping']  # g/l
        self.H2O_stripping = self.df['value'].loc['H2O_stripping']
        self.LiCl = self.LiCl_conc_stripping * self.plant.brine_flow_day * 10**3 /24 * self.plant.plant_uptime * \
                    self.column.Li_recovery  # g
        self.LiCl_sol_output = self.LiCl / self.LiCl_conc_stripping  # l
        return

if __name__ == '__main__':
    test = ColumnExtractionStripping()
    print(test)