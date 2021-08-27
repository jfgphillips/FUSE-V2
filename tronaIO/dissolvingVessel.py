import pandas as pd
from calculators.QProcesses import stirring_energy

class dissolvingVessel:
    def __init__(self):
        df = pd.read_excel(r'../data/trona_attributes.xlsx', sheet_name="dissolving vessel", skiprows=1)
        df.set_index('key', inplace=True)
        self.temperature = df['value'].loc['temperature']
        self.time = df['value'].loc['residence time']
        #self.volume = df['value'].loc['reactor volume']
        self.density = df['value'].loc['density']
        self.efficiency = df['value'].loc['efficiency']
        self.energyConsumption = self.qMachine()

    def qMachine(self):
        a = 0
        b = 0
        c = 0
        energyConsumption = stirring_energy(a,b,c,self.density, self.time,self.efficiency)
        return energyConsumption


