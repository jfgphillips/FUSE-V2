import pandas as pd
from Geothermal_IO.LDH import Plant
from Geothermal_IO.LDH import Column
from Geothermal_IO.LDH import Brine
from calculators import unitConversions as uC


class ForwardOsmosis(object):
    def __init__(self):
        self.plant = Plant.Plant_att()
        self.column = Column.Column_att()
        self.brine = Brine.Brine_att()
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name='FO', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.efficiency = self.df['value'].loc['efficiency']
        self.Li_conc_FO = self.df['value'].loc['Li_conc_FO']
        self.Li_conc_FO_mol = uC.solidMol('Li', self.Li_conc_FO)
        self.LiCl_conc_stripping_mol = self.Li_conc_FO_mol
        self.LiCl_conc_FO = uC.solidMass('LiCl', self.LiCl_conc_stripping_mol)
        self.LiCl_conc_stripping = uC.solidMass('LiCl', self.LiCl_conc_stripping_mol)
        self.Li_FO = self.brine.Li_conc_brine * self.plant.brine_flow_day * 10 ** 3 / 24 * self.plant.plant_uptime * \
                            self.column.Li_recovery  # g
        self.Li_sol_output = self.Li_FO / self.Li_conc_FO  # l
        return

if __name__ == '__main__':
    test = ForwardOsmosis()
    print(test)