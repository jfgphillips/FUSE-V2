import numpy as np
from SolvayIO.machinesIO.calciner import *




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

    return Na2CO3, water, cacliner_CO2


def qMachine(machine_properties):
    energyConsumption = 100  # kW
    return energyConsumption



