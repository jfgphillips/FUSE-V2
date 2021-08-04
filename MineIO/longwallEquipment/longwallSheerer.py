import pandas as pd
from calculators.QMachines import poweredVehicle


class longwallShearer_att:
    def __init__(self):
        df= pd.read_excel(r'../data/mine_attributes.xlsx', sheet_name="longwall shearer", skiprows=1)
        df.set_index('key', inplace=True)
        self.production_output = df['value'].loc["production output"]
        self.power = df['value'].loc["power"]
        self.workers = df['value'].loc["workers"]
        return

def qMachine(power=None, required_output=None, prod_output=None, usage=None, units=None):
    miner_factor = required_output/prod_output
    emissions = poweredVehicle(power, usage, units) * miner_factor
    return emissions
