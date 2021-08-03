import pandas as pd
from calculators.QMachines import poweredVehicle

class roofBolter_att(object):

    def __init__(self):
        df = pd.read_excel(r'../data/mine_attributes.xlsx', sheet_name="roof bolter", skiprows=1)
        df.set_index('key', inplace=True)
        self.model = df['value'].loc['model']
        self.power = df['value'].loc['power']
        self.workers = df['value'].loc['workers']
        return


def qMachine(power, usage, units):
    emissions = poweredVehicle(power, usage, units)
    return emissions