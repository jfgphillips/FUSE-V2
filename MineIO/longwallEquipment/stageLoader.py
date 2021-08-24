import pandas as pd
from calculators.QMachines import haulageVehicle


class stageLoader_att:
    def __init__(self):
        df = pd.read_excel(r'../data/mine_attributes.xlsx', sheet_name="stage loader", skiprows=1)
        df.set_index('key', inplace=True)
        self.power = df['value'].loc['power']
        self.workers = df['value'].loc['workers']
        self.max_output = df['value'].loc['max output'] #TPH


def qMachine(power=None, load=None, rating=None, usage=None, units=None):
    emissions = haulageVehicle(power, load, rating, usage, units)
    return emissions


