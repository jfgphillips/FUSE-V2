import numpy as np
from SolvayIO.machinesIO.slacker import *




def reaction(CaO, water, YIELD):
    """
    CaO + H2O --> Ca(OH)2
    :param YIELD:
    :param CaO: moles CaO
    :param water: moles H20
    :return:
    """
    YIELD = 1

    slack_lime = CaO * YIELD
    return slack_lime


def qMachine(machine_properties):
    energyConsumption = 100  #kW
    return energyConsumption