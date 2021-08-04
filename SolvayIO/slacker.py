import pandas as pd


class slacker_att(object):
    def __init__(self):
        df = pd.read_excel(r'../data/solvay_attributes.xlsx', sheet_name="slacker", skiprows=1)
        df.set_index('key', inplace=True)
        self.temperature = df['value'].loc['temperature']
        self.time = df['value'].loc['residence time']
        return

def reaction(CaO=None, H20=None):
    """
    CaO + H2O --> Ca(OH)2
    :param YIELD:
    :param CaO: moles CaO
    :param H20: moles H20
    :return:
    """
    YIELD = 1
    if CaO > H20:
        limiting_reagent = H20
    elif H20 > CaO:
        limiting_reagent = CaO

    products = {"Ca(OH)2":limiting_reagent * YIELD}
    return products

def revReaction(slacked_lime):
    """
    CaO + H2O <-- Ca(OH)2
    :param slacked_lime:
    :return:
    """
    YIELD = 1
    CaO = slacked_lime * YIELD
    H20 = slacked_lime * YIELD
    req_reactants = {"CaO": CaO, "H20": H20}
    return req_reactants

def qMachine(machine_properties):
    energyConsumption = 100  #kW
    return energyConsumption