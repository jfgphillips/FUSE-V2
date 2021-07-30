import pandas as pd
from calculators.QReactors import tubeFurnace


class limeKiln_att(object):
    def __init__(self):
        df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/solvay_attributes.xlsx', sheet_name="lime kiln", skiprows=1)
        df.set_index('key', inplace=True)
        self.temperature = df['value'].loc['temperature']
        self.time = df['value'].loc['residence time']
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


def revReaction(calcium_oxide):
    """
    CaCO3 <-- CaO + CO2
    :param calcium_oxide:
    :return:
    """
    YIELD = 1
    CaCO3 = calcium_oxide * YIELD
    CO2 = calcium_oxide * YIELD
    req_reactants = {"CaCO3": CaCO3}
    byproducts = {"CO2": CO2}
    return req_reactants, byproducts



def qMachine(machine_properties):
    density_CaCO3 = 2.71  # g/cm^3
    weighted_av_density = density_CaCO3
    energyConsumption = tubeFurnace(machine_properties.temperature, machine_properties.time, machine_properties.volume,
                                    weighted_av_density)
    return energyConsumption