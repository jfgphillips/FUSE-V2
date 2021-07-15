import numpy as np
import pandas as pd
from calculators.QMachines import poweredVehicle


class continuousMiner_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="continuous miner", skiprows=1)
        self.df.set_index('key', inplace=True)
        # print(self.df.index)
        self.production_output = self.df['value'].loc["production output"]
        self.power = self.df['value'].loc["power"]
        self.workers = self.df['value'].loc['workers']
        return


def qMachine(power, required_output, prod_output, usage, units):
    miner_factor = required_output/prod_output
    emissions = poweredVehicle(power, usage, units) * miner_factor

    return emissions
