import numpy as np
from SolvayIO.machinesIO.limeKiln import *



def reaction(limestone, coke, YIELD):
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

    return quick_lime, CO_2


def qMachine(machine_properties):
    energyconsumption = 100  #kW
    return energyconsumption


