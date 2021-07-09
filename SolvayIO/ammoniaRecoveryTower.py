import pandas as pd
import numpy as np


class ammoniaRecTower_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/solvay_attributes.xlsx', sheet_name="ammonia recovery tower", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.temperature = self.df['value'].loc['temperature']
        self.time = self.df['value'].loc['residence time']
        return

def reaction(slacked_lime, ammonium_chloride):
    """
    2 NH4Cl + Ca(OH)2 --> CaCl2 + 2 NH3 + 2 H20
    :param slacked_lime: concentration of slacked lime in solution
    :param ammonium_chloride: concentration of ammonium chloride
    :param YIELD: efficiency of the step
    :return:
    """
    YIELD = 1
    if slacked_lime >= ammonium_chloride:
        limiting_reagent = ammonium_chloride/2
    elif ammonium_chloride > slacked_lime:
        limiting_reagent = slacked_lime

    cal_chloride = limiting_reagent * 1 * YIELD
    rec_ammonia = limiting_reagent * 2 * YIELD
    recycled_water = limiting_reagent * 2 * YIELD

    products = {"NH3": rec_ammonia, "H2O": recycled_water}
    waste = {"CaCl2":cal_chloride}

    return products, waste

def revReaction(ammonium_chloride):
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