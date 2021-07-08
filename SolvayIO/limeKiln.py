import pandas as pd
from calculators.QReactors import tubeFurnace


class limeKiln_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/solvay_attributes.xlsx', sheet_name="lime kiln", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.temperature = self.df['value'].loc['temperature']
        self.time = self.df['value'].loc['residence time']
        return

def reaction(limestone):
    """
    CaCO3 --> CaO + CO2
    :param limestone: mass limestone
    :param coke: mass coke
    :param YIELD:
    :return:
    """
    YIELD = 1

    quick_lime = limestone * YIELD
    CO_2 = limestone * YIELD

    products = {"CaO": quick_lime, "kiln_CO_2": CO_2}

    return products


def qMachine(machine_properties):
    density_CaCO3 = 2.71  # g/cm^3
    weighted_av_density = density_CaCO3
    energyConsumption = tubeFurnace(machine_properties.temperature, machine_properties.time, machine_properties.volume,
                                    weighted_av_density)
    return energyConsumption