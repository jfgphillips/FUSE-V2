import pandas as pd


class slacker_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/solvay_attributes.xlsx', sheet_name="slacker", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.temperature = self.df['value'].loc['temperature']
        self.time = self.df['value'].loc['residence time']
        return

def reaction(CaO, water):
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