import numpy as np
from SolvayIO.machinesIO.ammoniaRecoveryTower import *


def reaction(slacked_lime, ammonium_chloride):
    """
    2 NH4Cl + Ca(OH)2 --> CaCl2 + 2 NH3 + 2 H20
    :param slacked_lime: concentration of slacked lime in solution
    :param ammonium_chloride: concentration of ammonium chloride
    :param YIELD: efficiency of the step
    :return:
    """
    YIELD = 1

    limiting_reagent = ammonium_chloride/2
    cal_chloride = limiting_reagent * 1 * YIELD
    rec_ammonia = limiting_reagent * 2 * YIELD
    recycled_water = limiting_reagent * 2 * YIELD

    return cal_chloride, rec_ammonia, recycled_water

def qMachine(machine_properties):
    energyConsumption = 100  #kW
    return energyConsumption


