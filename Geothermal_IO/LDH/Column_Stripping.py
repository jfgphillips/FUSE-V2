import pandas as pd
from Geothermal_IO.LDH import Plant
from Geothermal_IO.LDH import Column
from Geothermal_IO.LDH import Brine
from calculators import unitConversions as uC


class ColumnExtractionStripping(object):
    def __init__(self):
        self.plant = Plant.Plant_att()
        self.column = Column.Column_att()
        self.brine = Brine.Brine_att()
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name='stripping', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.Li_conc_stripping = self.df['value'].loc['Li_conc_stripping']  # g/l
        self.Li_conc_stripping_mol = uC.solidMol('Li', self.Li_conc_stripping)
        self.LiCl_conc_stripping_mol = self.Li_conc_stripping_mol
        self.LiCl_conc_stripping = uC.solidMass('LiCl', self.LiCl_conc_stripping_mol)
        self.H2O_stripping = self.df['value'].loc['H2O_stripping']
        self.Li_extracted = self.brine.Li_conc_brine * self.plant.brine_flow_day * 10**3 /24 * self.plant.plant_uptime * \
                    self.column.Li_recovery  # g
        self.Li_sol_output = self.Li_extracted / self.Li_conc_stripping  # l
        return

if __name__ == '__main__':
    test = ColumnExtractionStripping()
    print(test)