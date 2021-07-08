import pandas as pd
from calculators.QReactors import tubeFurnace

class calciner_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/solvay_attributes.xlsx', sheet_name="calciner", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.temperature = self.df['value'].loc['temperature']
        self.time = self.df['value'].loc['residence time']
        self.volume = self.df['value'].loc['reactor volume']
        return


def reaction(sodium_bicarbonate):
    """
    2NaHCO3 --> Na2CO3 + H20 + CO2
    :param sodium_bicarbonate:
    :param machine_properties:
    :return:
    """
    YIELD = 1

    Na2CO3 = sodium_bicarbonate / 2 * YIELD
    water = sodium_bicarbonate / 2 * YIELD
    cacliner_CO2 = sodium_bicarbonate / 2 * YIELD
    products = {"Na2CO3":Na2CO3, "water":water,"cacliner_CO2":cacliner_CO2}

    return products


def qMachine(machine_properties):
    density_NaHCO3 = 2.2
    weighted_av_density = density_NaHCO3
    energyConsumption = tubeFurnace(machine_properties.temperature,machine_properties.time,machine_properties.volume,weighted_av_density)  # kW
    return energyConsumption