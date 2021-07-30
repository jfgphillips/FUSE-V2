import numpy as np
import pandas as pd
from calculators.QMachines import poweredVehicle


class continuousMiner_att(object):
    def __init__(self):
        df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="continuous miner", skiprows=1)
        df.set_index('key', inplace=True)
        # print(self.df.index)
        self.production_output = df['value'].loc["production output"]
        self.power = df['value'].loc["power"]
        self.workers = df['value'].loc['workers']
        return


def qMachine(power, required_output, prod_output, usage, units):
    miner_factor = required_output/prod_output
    emissions = poweredVehicle(power, usage, units) * miner_factor

    return emissions
