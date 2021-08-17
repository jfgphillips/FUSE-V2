import pandas as pd

class SorbentSynthesisEquipment(object):
    def __init__(self):
        self.df = pd.read_excel(r'\Users\chant\PycharmProjects\FUSE-V2\data\LDH_attributes.xlsx',
                                sheet_name="equipment", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.reactor_FOB = self.df['FOB'].loc['reactor with agitator']
        self.reactor_size_base = self.df['size base'].loc['reactor with agitator']
        self.reactor_size_ref = self.df['size ref'].loc['reactor with agitator']
        self.reactor_size_factor = self.df['n'].loc['reactor with agitator']
        self.filter_FOB = self.df['FOB'].loc['filter']
        self.filter_size_base = self.df['size base'].loc['filter']
        self.filter_size_ref = self.df['size ref'].loc['filter']
        self.filter_size_factor = self.df['n'].loc['filter']
        self.grinder_FOB = self.df['FOB'].loc['grinder']
        self.grinder_size_base = self.df['size base'].loc['grinder']
        self.grinder_size_ref = self.df['size ref'].loc['grinder']
        self.grinder_size_factor = self.df['n'].loc['grinder']
        self.grinder_FOB = self.df['FOB'].loc['grinder']
        self.grinder_size_base = self.df['size base'].loc['grinder']
        self.grinder_size_ref = self.df['size ref'].loc['grinder']
        self.grinder_size_factor = self.df['n'].loc['grinder']
        self.pump_FOB = self.df['FOB'].loc['pump']
        self.pump_size_base = self.df['size base'].loc['pump']
        self.pump_size_ref = self.df['size ref'].loc['pump']
        self.pump_size_factor = self.df['n'].loc['pump']
        self.valve_FOB = self.df['FOB'].loc['valve']
        self.valve_size_base = self.df['size base'].loc['valve']
        self.valve_size_ref = self.df['size ref'].loc['valve']
        self.valve_size_factor = self.df['n'].loc['valve']
        self.pipe_FOB = self.df['FOB'].loc['pipe']
        self.pipe_size_base = self.df['size base'].loc['pipe']
        self.pipe_size_ref = self.df['size ref'].loc['pipe']
        self.pipe_size_factor = self.df['n'].loc['pipe']
        self.pipe_amount = self.df['amount'].loc['pipe']
        self.CEPCI_base = self.df['machine'].loc['CEPCI base']
        return


def cost_equipment(FOB, CEPCI_base, size_base, size_ref, size_factor):
    """
    Source: Huang 2021, Life Cycle Assessment and Techno-Economic Assessment of Lithium Recovery from Geothermal
    Brines, Supporting Information
    Including 10% increase for delivery cost
    :return:
    """
    CEPCI_ref = 1000
    cost_base = 1.1 * FOB * (CEPCI_base / CEPCI_ref) * (size_base / size_ref)**size_factor
    return cost_base

