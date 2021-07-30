import pandas as pd


class ammoniaSaturator_att(object):
    def __init__(self):
        df = pd.read_excel(r'../data/solvay_attributes.xlsx', sheet_name="ammonia saturator", skiprows=1)
        df.set_index('key', inplace=True)
        self.temperature = df['value'].loc['temperature']
        self.time = df['value'].loc['residence time']
        return


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
    saturated_soln = {"NaCl":NaCl*YIELD, "NH3": ammonia*YIELD}

    return saturated_soln


def qMachine(machine_properties):
    energyConsumption = 100  # kW
    return energyConsumption
