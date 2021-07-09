import pandas as pd


class filter_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/solvay_attributes.xlsx', sheet_name="filter", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.temperature = self.df['value'].loc['temperature']
        self.time = self.df['value'].loc['residence time']
        return

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

