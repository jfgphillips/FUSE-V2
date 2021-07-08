import pandas as pd


class limeKiln_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/solvay_attributes.xlsx', sheet_name="lime kiln", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.temperature = self.df['value'].loc['temperature']
        self.time = self.df['value'].loc['residence time']
        return

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