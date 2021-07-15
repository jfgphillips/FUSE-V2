from calculators.QMachines import haulageVehicle
import pandas as pd

class LHD_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx', sheet_name="LHD", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.model = self.df['value'].loc['model']
        self.power = self.df['value'].loc['power']
        self.workers = self.df['value'].loc['workers']
        self.nameplate_rating = self.df['value'].loc['nameplate rating']


def qMachine(power, load, rating, usage, units):
    emissions = haulageVehicle(power, load, rating, usage, units)

    return emissions
