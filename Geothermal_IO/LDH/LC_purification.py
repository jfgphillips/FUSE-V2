import pandas as pd
from calculators import unitConversions


class LiCarbonatePurification_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name='Li2CO3_purification', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.CO2_excess = self.df['value'].loc['CO2_excess']
        self.Yield_forward = self.df['value'].loc['yield_forward']
        self.Yield_backward = self.df['value'].loc['yield_backward']
        self.carbonation_temp = self.df['value'].loc['carbonation_temp']
        self.carbonation_pressure = self.df['value'].loc['carbonation_pressure']
        self.carbonation_time = self.df['value'].loc['carbonation_time']
        self.precipitation_temp = self.df['value'].loc['precipitation_temp']
        self.precipitation_pressure = self.df['value'].loc['precipitation_pressure']
        self.precipitation_time = self.df['value'].loc['precipitation_time']
        self.thermal_conductivity = self.df['value'].loc['thermal_conductivity_reactor']
        self.wall_thickness = self.df['value'].loc['wall_thickness']
        self.surface_area = self.df['value'].loc['surface_area']
        self.mass_difference_evaporation = self.df['value'].loc['mass_difference_evaporation']
        self.dryer_efficiency = self.df['value'].loc['dryer_efficiency']
        self.washing_temperature = self.df['value'].loc['washing_temperature']
        return


def QReactants(mol_Li2CO3=None, hc_Li2CO3=None, mol_H2O=None, hc_H2O=None, mol_CO2=None, hc_CO2=None,
               reaction_temperature=None):
    """
    source: Sharma 2020
    """
    room_temperature = 298.15 #K
    q_reactants_joule = (mol_Li2CO3 * hc_Li2CO3 * (reaction_temperature - room_temperature) +
                         mol_CO2 * hc_CO2 * (reaction_temperature - room_temperature) +
                         mol_H2O * hc_H2O * (reaction_temperature - room_temperature))
    q_reactants_kWh = unitConversions.kiloWattHours(q_reactants_joule)
    return q_reactants_kWh


def Purification_raction(Li2CO3_impure=None, CO2_excess=None, Yield_forward=None, Yield_backward=None):
    """
    Li2CO3_impure + H2O + CO2(excess) --> 2 LiHCO3
    2 LiH2O3 + heat --> Li2CO3(pure) + H2O + 2 CO2
    :param Li2CO3_impure: impure LiCO2 from LiCO2 processing
    :param CO2_excess: excess of CO2 used in this reaction
    :param Yield: yield of the prufication process
    :return: amount of pure Li2CO3 produced
    """
    Li2CO3_impure_grams = unitConversions.grams(Li2CO3_impure)
    mol_Li2CO3_impure = unitConversions.solidMol('Li2CO3', Li2CO3_impure_grams)
    mol_H2O = mol_Li2CO3_impure
    mass_H2O = unitConversions.solidMass('H2O', mol_H2O)
    mol_CO2 = mol_Li2CO3_impure * CO2_excess
    mass_CO2 = unitConversions.solidMass('CO2', mol_CO2)
    mol_LiHCO3 = 2 * mol_Li2CO3_impure * Yield_forward
    mass_LiHCO3 = unitConversions.solidMass('LiHCO3', mol_LiHCO3)
    mol_Li2CO3_pure = mol_Li2CO3_impure * Yield_forward * Yield_backward
    mass_Li2CO3_pure = unitConversions.solidMass('Li2CO3', mol_Li2CO3_pure)
    mol_CO2_product = mol_Li2CO3_impure * Yield_forward * Yield_backward
    mass_CO2_product = unitConversions.solidMass('CO2', mol_CO2_product)
    mol_H2O_product = mol_Li2CO3_impure * Yield_forward * Yield_backward
    mass_H2O_product = unitConversions.solidMass('H2O', mol_H2O_product)
    reactants = {'impure Li2CO3': Li2CO3_impure_grams, 'H2O': mass_H2O, 'CO2': mass_CO2}
    intermediate = {'LiHCO3': mass_LiHCO3}
    product = {'pure Li2CO3': mass_Li2CO3_pure}
    by_products = {'CO2': mass_CO2_product, 'H2O': mass_H2O_product}
    return reactants, intermediate, product, by_products


def Purification_revreaction(Li2CO3_pure=None, CO2_excess=None, Yield=None):
    """
    Li2CO3_impure + H2O + 2 CO2 (excess) --> 2 LiHCO3
    2 LiH2O3 + heat --> Li2CO3(pure) + H2O + 2 CO2

    :param Li2CO3_pure: pure (>99.5%) Li2CO3 product in tpy
    :param CO2_excess: excess of CO2 used in this reaction
    :param Yield: yield of the prufication process
    :return: amount of impure Li2CO3 and other reactants needed
    """
    Li2CO3_pure_grams = unitConversions.grams(Li2CO3_pure)
    mol_LiCO3_pure = unitConversions.solidMol('Li2CO3', Li2CO3_pure_grams)
    mol_Li2CO3_impure = mol_LiCO3_pure / Yield
    mass_Li2CO3_impure = unitConversions.solidMass('Li2CO3', mol_Li2CO3_impure)
    H2O_mol = mol_Li2CO3_impure
    H2O_mass = unitConversions.solidMass('H2O', H2O_mol)
    CO2_mol = mol_Li2CO3_impure * CO2_excess
    CO2_mass = unitConversions.solidMass('CO2', CO2_mol)
    reactants = {'impure_Li2CO3': mass_Li2CO3_impure, 'H2O': H2O_mass, 'CO2': CO2_mass}
    return reactants

if __name__ == '__main__':
    test = LiCarbonatePurification_att()
    print(test)
