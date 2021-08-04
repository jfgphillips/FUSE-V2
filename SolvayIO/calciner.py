import pandas as pd
from calculators.QReactors import tubeFurnace

class calciner_att(object):
    def __init__(self):
        df = pd.read_excel(r'../data/solvay_attributes.xlsx', sheet_name="calciner", skiprows=1)
        df.set_index('key', inplace=True)
        self.temperature = df['value'].loc['temperature']
        self.time = df['value'].loc['residence time']
        self.volume = df['value'].loc['reactor volume']
        return


def reaction(sodium_bicarbonate=None):
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
    products = {"Na2CO3":Na2CO3, "H20": water,"CO2":cacliner_CO2}

    return products

def revReaction(soda_ash=None):
    """
    2NaHCO3 <-- Na2CO3 + H20 + CO2
    :param soda_ash:
    :return:
    """
    YIELD = 1
    sodium_bicarbonate = soda_ash * 2 * YIELD

    return sodium_bicarbonate


def qMachine(machine_properties=None):
    density_NaHCO3 = 2.2
    weighted_av_density = density_NaHCO3
    energyConsumption = tubeFurnace(machine_properties.temperature,machine_properties.time,machine_properties.volume, weighted_av_density)  # kW
    return energyConsumption
