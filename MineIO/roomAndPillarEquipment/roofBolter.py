import pandas as pd
from calculators.QMachines import poweredVehicle

class roofBolter_att(object):

    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="roof bolter", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.model = self.df['value'].loc['model']
        self.power = self.df['value'].loc['power']
        self.workers = self.df['value'].loc['workers']
        return


def qMachine(power, usage, units):
    emissions = poweredVehicle(power, usage, units)

    return emissions