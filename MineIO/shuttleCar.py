import pandas as pd
from calculators.QMachines import haulageVehicle

class shuttleCar_att(object):

    def __init__(self):
        df = pd.read_excel(r'../data/mine_attributes.xlsx', sheet_name="shuttle car", skiprows=1)
        df.set_index('key', inplace = True)
        self.model = df['value'].loc['model']
        self.nameplate_rating = df['value'].loc['nameplate rating']
        self.power = df['value'].loc['power']
        self.workers = df['value'].loc['workers']
        return


def qMachine(power=None, load=None, rating=None, usage=None, units=None):
    emissions = haulageVehicle(power, load, rating, usage, units)
    return emissions
