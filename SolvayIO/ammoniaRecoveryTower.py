import pandas as pd
import numpy as np


class ammoniaRecTower_att(object):
    def __init__(self):
        df = pd.read_excel(r'../data/solvay_attributes.xlsx', sheet_name="ammonia recovery tower", skiprows=1)
        df.set_index('key', inplace=True)
        self.temperature = df['value'].loc['temperature']
        self.time = df['value'].loc['residence time']
        return

def reaction(CaOH2=None, NH4Cl=None):
    """
    2 NH4Cl + Ca(OH)2 --> CaCl2 + 2 NH3 + 2 H20
    :param CaOH2: concentration of slacked lime in solution
    :param NH4Cl: concentration of ammonium chloride
    :param YIELD: efficiency of the step
    AMMONIARECOVERY source: https://chemicalengineeringfacts.wordpress.com/2017/01/17/chemical-technology/

    :return:
    """
    YIELD = 1
    AMMONIARECOVERY = 0.98
    if CaOH2 >= NH4Cl:
        limiting_reagent = NH4Cl / 2
    elif NH4Cl > CaOH2:
        limiting_reagent = CaOH2

    cal_chloride = limiting_reagent * 1 * YIELD
    rec_ammonia = limiting_reagent * 2 * AMMONIARECOVERY
    recycled_water = limiting_reagent * 2 * YIELD

    products = {"NH3": rec_ammonia, "H2O": recycled_water}
    waste = {"CaCl2":cal_chloride}

    return products, waste

def revReaction(ammonium_chloride=None):
    """
    2 NH4Cl + Ca(OH)2 --> CaCl2 + 2 NH3 + 2 H20
    :param ammonium_chloride:
    :return:
    """
    YIELD = 1
    slacked_lime = ammonium_chloride/2 * YIELD
    cal_chloride = ammonium_chloride/2 * YIELD
    ammonia = ammonium_chloride * YIELD
    water = ammonium_chloride * YIELD
    req_reactants = {"Ca(OH)2": slacked_lime}
    waste = {"CaCl2": cal_chloride}
    byproducts = {"NH3":ammonia, "H2O":water}

    return req_reactants, byproducts, waste


def qMachine(machine_properties):
    energyConsumption = 100  #kW
    return energyConsumption