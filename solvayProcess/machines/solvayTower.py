import numpy as np
from SolvayIO.machinesIO.solvayTower import *

def reaction(saturated_soln, sum_CO_2):
    """
    NaCl + NH3 + CO2 + H2O --> NaHCO3 + NH4Cl
    :param saturated_soln: contains NaCl and NH3
    :param sum_CO_2: total CO2
    :param YIELD:
    :return:
    """
    YIELD = 1
    NaCl = saturated_soln["NaCl"]
    NH3 = saturated_soln["NH3"]
    H2O = saturated_soln["H2O"]
    limiting_reagent = NaCl
    reacted_solution = {"NaHCO3": limiting_reagent * YIELD, "NH4Cl": limiting_reagent * YIELD}

    return reacted_solution


def qMachine(machine_properties):
    energyConsumption = 100  #kW
    return energyConsumption
