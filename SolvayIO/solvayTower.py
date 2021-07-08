import pandas as pd


class solvayTower_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/solvay_attributes.xlsx', sheet_name="solvay tower", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.temperature = self.df['value'].loc['temperature']
        self.time = self.df['value'].loc['residence time']
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


def qMachine(machine_properties):
    energyConsumption = 100  #kW
    return energyConsumption