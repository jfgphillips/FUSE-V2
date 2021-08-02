import pandas as pd


class solvayTower_att(object):
    def __init__(self):
        df = pd.read_excel(r'../data/solvay_attributes.xlsx', sheet_name="solvay tower", skiprows=1)
        df.set_index('key', inplace=True)
        self.temperature = df['value'].loc['temperature']
        self.time = df['value'].loc['residence time']
        return

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
    #  H2O = saturated_soln["H2O"] TODO: implement a water value into saturated_soln
    if NaCl > NH3 and sum_CO_2 > NH3:
        limiting_reagent = NH3
    elif NH3 > NaCl and sum_CO_2 > NaCl:
        limiting_reagent = NaCl
    else:
        limiting_reagent = sum_CO_2
    reacted_solution = {"NaHCO3": limiting_reagent * YIELD, "NH4Cl": limiting_reagent * YIELD}

    return reacted_solution

def revReaction(sodium_bicarbonate):
    """
    NaCl + NH3 + CO2 + H2O <-- NaHCO3 + NH4Cl
    :param sodium_bicarbonate:
    :return:
    """
    YIELD = 1
    water = sodium_bicarbonate * YIELD
    CO2 = sodium_bicarbonate * YIELD
    NH3 = sodium_bicarbonate * YIELD
    NaCl = sodium_bicarbonate * YIELD
    NH4Cl = sodium_bicarbonate * YIELD

    req_reactants = {"NH3": NH3, "NaCl": NaCl, "CO2":CO2, "H2O": water}
    byproducts = {"NH4Cl": NH4Cl}
    return req_reactants, byproducts


def qMachine(machine_properties):
    energyConsumption = 100  #kW
    return energyConsumption