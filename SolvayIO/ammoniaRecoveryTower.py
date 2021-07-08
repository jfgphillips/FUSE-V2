import pandas as pd


class ammoniaRecTower_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'/Users/john/Documents/University Work/summer internship/FUSE/data/solvay_attributes.xlsx', sheet_name="ammonia recovery tower", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.temperature = self.df['value'].loc['temperature']
        self.time = self.df['value'].loc['residence time']
        return

def reaction(slacked_lime, ammonium_chloride):
    """
    2 NH4Cl + Ca(OH)2 --> CaCl2 + 2 NH3 + 2 H20
    :param slacked_lime: concentration of slacked lime in solution
    :param ammonium_chloride: concentration of ammonium chloride
    :param YIELD: efficiency of the step
    :return:
    """
    YIELD = 1

    limiting_reagent = ammonium_chloride/2
    cal_chloride = limiting_reagent * 1 * YIELD
    rec_ammonia = limiting_reagent * 2 * YIELD
    recycled_water = limiting_reagent * 2 * YIELD

    return cal_chloride, rec_ammonia, recycled_water

def qMachine(machine_properties):
    energyConsumption = 100  #kW
    return energyConsumption