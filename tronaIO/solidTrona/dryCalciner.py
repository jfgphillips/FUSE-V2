import pandas as pd
from calculators.QReactors import tubeFurnace

class dryCalciner:
    def __init__(self):
        """
        particle size = 6.35mm TODO: add a crusher before this between the plant
        """
        df = pd.read_excel(r'../data/trona_attributes.xlsx', sheet_name="dryCalciner", skiprows=1)
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

