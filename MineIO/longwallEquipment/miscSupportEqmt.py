import pandas as pd
from calculators.QMachines import beltConveyor

class tShield_att:
    def __init__(self):
        df = pd.read_excel(r'../data/mine_attributes.xlsx', sheet_name="t shield", skiprows=1)

class afc_att:
    def __init__(self):
        df = pd.read_excel(r'../data/mine_attributes.xlsx', sheet_name="AFC", skiprows=1)
        df.set_index('key', inplace=True)
        self.drive_power = df['value'].loc['drive_power']
        self.model = df['value'].loc['model']
        self.workers = df['value'].loc['workers']


    def qMachine(self): # TODO: extrapolate belt speed from the mine output
        energyConsumption = beltConveyor()
        return energyConsumption


class flatLinkChain_att:
    def __init__(self):
        df = pd.read_excel(r'../data/mine_attributes.xlsx', sheet_name="flat link chain", skiprows=1)

class lowProfileChain_att:
    def __init__(self):
        df = pd.read_excel(r'../data/mine_attributes.xlsx', sheet_name="low profile chain", skiprows=1)

