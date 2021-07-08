import numpy as np
from SolvayIO.machinesIO.ammoniaSaturator import *


def reaction(NaCl, ammonia):
    """
    NaCl
    NH3
    --> NaCl + NH3
    :param brine:
    :param ammonia:
    :param YIELD:
    :return:
    """
    YIELD = 1
    saturated_soln = {"NaCl":NaCl, "NH3": ammonia}

    return saturated_soln


def qMachine(machine_properties):
    energyConsumption = 100  # kW
    return energyConsumption


properties = ammoniaSaturator_att
qMachine(properties)
