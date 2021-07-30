import pandas as pd
from calculators.QMachines import haulageVehicle

class shuttleCar_att(object):

    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="shuttle car", skiprows=1)
        self.df.set_index('key', inplace = True)
        self.model = self.df['value'].loc['model']
        self.nameplate_rating = self.df['value'].loc['nameplate rating']
        self.power = self.df['value'].loc['power']
        self.workers = self.df['value'].loc['workers']
        return


def qMachine(power, load, rating, usage, units):
    emissions = haulageVehicle(power, load, rating, usage, units)

    return emissions
