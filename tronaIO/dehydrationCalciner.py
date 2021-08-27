from calculators.QReactors import tubeFurnace
import pandas as pd


class dehydrationCalciner:
    def __init__(self):
        df = pd.read_excel(r'../data/trona_attributes.xlsx', sheet_name="dehydration", skiprows=1)
        df.set_index('key', inplace=True)
        self.temperature = df['value'].loc['temperature']
        self.time = df['value'].loc['residence time']
        self.volume = df['value'].loc['reactor volume']
        self.density = df['value'].loc['density']
        self.energyConsumption = self.qMachine()
        return

    def qMachine(self):
        energyConsumption = tubeFurnace(self.temperature, self.time, self.volume, self.density)
        return energyConsumption