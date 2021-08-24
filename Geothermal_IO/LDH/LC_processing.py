import pandas as pd
from calculators import unitConversions


class LiCarbonateProcessing_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name='Li2CO3_processing', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.Yield = self.df['value'].loc['yield']
        self.reaction_temp = self.df['value'].loc['reaction_temp']
        self.reaction_time = self.df['value'].loc['reaction_time']
        self.thermal_conductivity = self.df['value'].loc['thermal_conductivity_reactor']
        self.wall_thickness = self.df['value'].loc['wall_thickness']
        self.surface_area = self.df['value'].loc['surface_area']
        return


def QReactants(mol_LiCl=None, hc_LiCl=None, mol_Na2CO3=None, hc_Na2CO3=None, reaction_temperature=None):
    """
    source: Sharma 2020
    :param mol_LiCl: in mol
    :param hc_LiCl: in J/[mol*K]
    :param mol_Na2CO3: in mol
    :param hc_Na2CO3: in J/[mol*K]
    :param reaction_temperature: in K
    :return: energy required to heat reactants in kWh
    """
    room_temperature = 298.15 #K
    q_reactants_joule = (mol_LiCl * hc_LiCl * (reaction_temperature - room_temperature) +
                       mol_Na2CO3 * hc_Na2CO3 * (reaction_temperature - room_temperature))
    q_reactants_kWh = unitConversions.kiloWattHours(q_reactants_joule)
    return q_reactants_kWh


def Li2CO3_reaction (LiCl=None, Yield=None):
    """
    2 LiCl + Na2CO3 --> Li2CO2 + 2 NaCl

    :param LiCl: amount of LiCl from extraction in grams
    :param Yield: yield of the reaction
    :return: mass of (impure) Li2CO3 produced
    """
    mol_LiCl = unitConversions.solidMol('LiCl', LiCl)
    mol_Na2CO3 = 0.5 * mol_LiCl
    mass_Na2CO3 = unitConversions.solidMass('Na2CO3', mol_Na2CO3)
    mol_Li2CO3 = 0.5 * mol_LiCl * Yield
    mass_Li2CO3 = unitConversions.solidMass('Li2CO3', mol_Li2CO3)
    mol_NaCl = mol_LiCl * Yield
    mass_NaCl = unitConversions.solidMass('NaCl', mol_NaCl)
    reactants = {'LiCl': LiCl, 'Na2CO3': mass_Na2CO3}  # in g
    product = {'Li2CO3': mass_Li2CO3}  # in g
    waste = {'NaCl': mass_NaCl}  # in g
    return reactants, product, waste


if __name__ == '__main__':
    test = LiCarbonateProcessing_att()
    print(test)
