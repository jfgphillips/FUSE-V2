import numpy as np
from SolvayIO.machinesIO.filter import *



def reaction(reacted_solution):
    """
    :param reacted_solution: dict containing product
    :return:
    """
    EFFICIENCY = 1

    NH4Cl = reacted_solution["NH4Cl"] * EFFICIENCY
    NaHCO3 = reacted_solution["NaHCO3"] * EFFICIENCY

    return NH4Cl, NaHCO3


def qMachine(machine_properties):
    energyConsumption = 1  #kW
    return energyConsumption


