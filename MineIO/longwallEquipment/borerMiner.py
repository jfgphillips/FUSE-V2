import pandas as pd
from calculators.QMachines import poweredVehicle

class borerMiner_att:
    def __init__(self):
        df = pd.read_excel(r'../data/mine_attributes.xlsx', sheet_name="borer miner", skiprows=1)
        df.set_index('key', inplace=True)
        self.production_output = df['value'].loc["production output"]
        self.power = df['value'].loc["power"]
        self.workers = df['value'].loc['workers']


def qMachine(power=None, usage=None, units=None):
    #miner_factor = required_output/prod_output
    emissions = poweredVehicle(power, usage, units) #* miner_factor
    return emissions
